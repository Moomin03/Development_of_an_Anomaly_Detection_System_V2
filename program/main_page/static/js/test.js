const selectButton = document.getElementById("select-button"); // 파일 선택 버튼
const fileInput = document.getElementById("file-input");
const uploadButton = document.getElementById("upload-button"); // 업로드 버튼
const removeButton = document.getElementById("remove-button"); // 파일 제거 버튼
const fileNameDisplay = document.getElementById("file-name"); // 파일 이름 표시 영역

// 파일 선택 버튼 클릭 시 파일 선택 창 열기
selectButton.addEventListener("click", function () {
    fileInput.click(); // 숨겨진 파일 선택 input 클릭
});

// 파일 선택 후 파일 정보 업데이트
fileInput.addEventListener("change", function () {
  if (fileInput.files.length > 0) { // 선택된 파일이 있는지 확인
    const fileNames = []; // 선택된 파일 이름 목록
    for (const file of fileInput.files) {
      fileNames.push(file.name); // 각 파일의 이름을 추가
    }
    fileNameDisplay.textContent = `${fileNames.join(", ")} File is Selected!`; // 파일 이름을 쉼표로 구분하여 표시
    fileNameDisplay.classList.remove("italic"); // 이탤릭 제거
    uploadButton.disabled = false; // 업로드 버튼 활성화
    removeButton.disabled = false; // 파일 제거 버튼 활성화
  } else {
    fileNameDisplay.textContent = "선택된 파일 없음"; // 선택된 파일이 없을 때의 메시지
    fileNameDisplay.classList.add("italic"); // 이탤릭 추가
    uploadButton.disabled = true; // 업로드 버튼 비활성화
    removeButton.disabled = true; // 파일 제거 버튼 비활성화
  }
});

// 파일 제거 버튼 클릭 시 파일 정보 초기화
removeButton.addEventListener("click", function () {
    fileInput.value = ""; // 파일 선택 값 초기화
    fileNameDisplay.textContent = "선택된 파일 없음"; // 선택된 파일 없음 표시
    uploadButton.disabled = true; // 업로드 버튼 비활성화
    removeButton.disabled = true; // 파일 제거 버튼 비활성화
});

// 업로드 버튼 클릭 시 업로드 준비 메시지 표시
uploadButton.addEventListener("click", function () {
        if (fileInput.files.length > 0) {
            const fileNames = []; // 선택된 파일 이름 목록
            for (const file of fileInput.files) {
                fileNames.push(file.name); // 각 파일의 이름을 추가
            }
            alert(`${fileNames.join(", ")} 파일이 업로드 되었습니다.\n"확인" 버튼을 누르시면 결과창에 악성 IP에 대한 로그를 반환합니다!`); // 업로드 준비 메시지
        }
});
