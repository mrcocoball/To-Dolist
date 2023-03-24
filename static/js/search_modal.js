// 모달 관련 변수
const searchModal = document.getElementById("searchModal")
const modalCallBtn = document.getElementById("searchModalCallBtn")
const cancelBtn = document.querySelector(".btn-close")

// 공유 버튼 클릭 시 공유하기 모달 표시
modalCallBtn.addEventListener("click", function (e) {
    console.log("modal invoke");
    searchModal.style.display = "flex";
}, false)


// 취소 버튼 클릭 시 모달 숨기기
cancelBtn.addEventListener("click", function (e) {
    console.log("modal hide");
    searchModal.style.display = "none";
}, false)