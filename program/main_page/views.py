from django.shortcuts import render

def test(request):
    return render(request, 'test.html')

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import io
import joblib
import datetime

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        content = uploaded_file.read().decode('utf-8')
        model = joblib.load('/Users/hack/PycharmProjects/Django/program/main_page/hardvoting.pkl')
        columns = ["ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p", "proto",
                   "service", "duration", "orig_bytes", "resp_bytes", "conn_state", "local_orig",
                   "local_resp", "missed_bytes", "history", "orig_pkts", "orig_ip_bytes", "resp_pkts",
                   "resp_ip_bytes", "tunnel_parents", "ip_proto"]
        df = pd.read_csv(io.StringIO(content), delimiter="\t", comment="#", skip_blank_lines=True)
        df.columns = columns
        df['orig_bytes'] = df['orig_bytes'].replace('-', 0).astype(int)
        df['orig_ip_bytes'] = df['orig_ip_bytes'].replace('-', 0).astype(int)
        df['src_bytes'] = df['orig_bytes'].astype(int) + df['orig_ip_bytes'].astype(int)
        df['service'] = df['service'].replace('-', 'unknown').astype(object)
        df['protocol_type'] = df['proto'].replace('-', 'unknown').astype(object)
        df['same_srv_rate'] = df.groupby('id.orig_h')['service'].transform(lambda x: x.eq(x.iloc[-1]).mean()).replace(
            '-', 0).astype(int)
        df['rerror_rate'] = df['conn_state'].apply(lambda x: 1 if x in ['REJ', 'S0'] else 0).replace('-', 0).astype(int)
        df['srv_rerror_rate'] = df.groupby('service')['conn_state'].transform(
            lambda x: x.isin(['REJ', 'S0']).mean()).replace('-', 0).astype(int)
        df['dst_host_srv_count'] = df.groupby('id.resp_h')['id.resp_h'].transform('count').replace('-', 0).astype(int)
        df['dst_host_same_src_port_rate'] = df.groupby('id.resp_h')['id.orig_p'].transform(
            lambda x: x.eq(x.iloc[-1]).mean()).replace('-', 0).astype(int)
        df['wrong_fragment'] = df['history'].apply(lambda x: 1 if 'f' in str(x) or 'r' in str(x) else 0).replace('-',
                                                                                                                 0).astype(
            int)
        df['dst_host_rerror_rate'] = df.groupby('id.resp_h')['conn_state'].transform(
            lambda x: x.isin(['REJ', 'S0']).mean()).replace('-', 0).astype(int)
        detected = [i for i in df.columns if i in model.feature_names_in_]
        remake_df = df[detected]
        remake_df = remake_df.reindex(columns=model.feature_names_in_, fill_value=0)
        result = model.predict(remake_df)  # 모델 예측 결과
        mapping_attack = {0: 'DOS_Attack', 1: 'NORMAL', 2: 'PROBING_Attack', 3: 'R2L_Attack', 4: 'U2R_Attack'}
        ip_addr = df['id.orig_h'].values  # 원본 데이터에서 IP 주소 가져오기

        # 공격이 의심스러운 결과만 필터링
        suspicious_ips = []
        track_time = df['ts'].apply(
            lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))  # ts를 datetime 형식으로 변환
        suspicious_ips.append('[System] 공격이 의심스러운 IP 주소 목록입니다.')
        for i in range(len(result)):
            if result[i] != 1:  # result[i]가 1이 아닌 경우에만 처리 (NORMAL 제외)
                suspicious_ips.append(f'[TL_V2] {track_time[i]} -> {ip_addr[i]}은 {mapping_attack[result[i]]} 공격 패턴을 보입니다.')

        # 리스트로 결과를 넘기기
        result_str = "\n".join(suspicious_ips)

        return render(request, 'test.html', {'file_content': result_str})
