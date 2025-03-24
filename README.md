## 🔍 ThreatLens_V2

<p align="center">
  <img src="https://github.com/Moomin03/Development_of_an_Anomaly_Detection-System/blob/master/LOGO.jpg" alt="이미지 설명" width="300" height="300">
</p>

<p align="center">
  <a href="https://hits.seeyoufarm.com">
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMoomin03%2FDevelopment_of_an_Anomaly_Detection-System%2F&count_bg=%2379C83D&title_bg=%23555555&icon=jupyter.svg&icon_color=%23E7E7E7&title=ThreatLens_V2&edge_flat=True" alt="Hits">
  </a>
</p>


## ThreatLens v2.0

> Development of an Anomaly Detection System for Web Log Data
>
> Development Period : 2025.02 ~ 2025.03


### ⚒️ Project Life Cycle
> Project Report : [↗️ 프로젝트 보고서](https://north-museum-b07.notion.site/NSL-KDD-1b90f748c6888065b6bae78168b3ae1d?pvs=4)
>
> Development Process : [↗️ 깃허브 레퍼지토리](https://github.com/Moomin03/Development_of_an_Anomaly_Detection_System_V2/tree/master)
>
> Model Deployment : [↗️ 개발 페이지 바로가기](https://github.com/Moomin03/Development_of_an_Anomaly_Detection_System_V2/blob/master/process/prcatice.ipynb)


### ⚒️ Project Introduction
**ThreatLens_V2 - Cybersecurity Anomaly Detection Trained by NSL-KDD Datasets**

ThreatLens_V2 is a cutting-edge project that combines data analysis and cybersecurity to detect and analyze abnormal access patterns in web logs. By utilizing real-world web log datasets from Kaggle, this project aims to identify anomalies such as unauthorized access attempts, abnormal traffic patterns, and potential threats based on IP addresses, user activity, and geolocation data.

**ThreatLens_V2 will give you a Powerful Strength**

1. To develop a machine learning model that can classify web traffic as normal or abnormal with high accuracy.
2. To provide insights into connection trends, including country-wise access patterns and suspicious behavior.
3. To enhance cybersecurity strategies by identifying and mitigating potential vulnerabilities in real-time.

This project has the potential to be expanded into a real-time anomaly detection system using live log data. Future plans include integrating with security monitoring systems to automate threat identification and response.

## 💻 Development Environment
- PC : Macbook Air M1 (2020)
- OS : Ubuntu (LTS 24.04)
- Python 3.9.0
- Tools : Jupyter Notebook


## ⚒️ Main Library
For building and running the application you need:
- scikit-learn : 1.5.2
- django : 4.2.20
- alibi : 0.9.6
- eli5 : 0.13.0
- other : ./requirements.txt


## ⚒️ How to Install?
```
# 저장될 파일을 만들어줘요!
ubuntu@ubuntu : mkdir 파일이름 
ubuntu@ubuntu : cd 파일이름
ubuntu@ubuntu: git clone https://github.com/Moomin03/Development_of_an_Anomaly_Detection-System_V2.git
ubuntu@ubuntu : cd Development_of_an_Anomaly_Detection-System_V2/

# 가상환경을 구축하고, requirement을 설치해요!
ubuntu@ubuntu : python -m venv 가상환경 이름
ubuntu@ubuntu : pip install -r requirements.txt

# 서버를 실행할거에요!
# 브라우저에서 localhost:8000/main_page로 접속해야해요(main_page만 구축되어있어요 ㅠ)!
ubuntu@ubuntu : cd program
ubuntu@ubuntu : python manage.py runserver

# 로그 데이터 준비 (우리는 Zeek(https://zeek.org/)를 사용할거에요!)
# 의존 패키지 설치
ubuntu@ubuntu : sudo apt install -y cmake make gcc g++ flex bison libpcap-dev \
    libssl-dev python3-dev swig zlib1g-dev
    
# Zeek 컴파일 및 설치
ubuntu@ubuntu : sudo apt install -y zeek
ubuntu@ubuntu : ./configure --prefix=/opt/zeek
ubuntu@ubuntu : make -j$(nproc) 
ubuntu@ubuntu : sudo make install
ubuntu@ubuntu : zeek --version(실행이 되지 않는 경우 아래 명령어를 작성해주세요!)
ubuntu@ubuntu : /opt/zeek/bin/zeek --version

# Log 데이터 수집하기 (라우터에 유선으로 연결한 후에, 포트미러링을 진행하면 라우터에 쌓이는 로그들을 수집할 수 있습니다.)
ubuntu@ubuntu : sudo zeek -i 인터넷망(eth0 / conn.log 수집 -> 명령어 오류시 아래 명령어로 작성해주세요.)
ubuntu@ubuntu : sudo /opt/zeek/bin/zeek -i 접속된 인터넷망(eth0 / conn.log 수집)

# 다음에 수집된 로그 데이터를 웹페이지 파일 올리기에 올려주시면 됩니다.
ubuntu@ubuntu : ls
```

## ⚒️ Project Map

![image](https://github.com/Moomin03/Development_of_an_Anomaly_Detection_System_V2/blob/master/image/Project_Map.png)