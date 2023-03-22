
const DOMAIN = 'http://localhost:9000/'

// 댓글 모달

const shareModal = document.getElementById("shareModal")
const modalCallBtn = document.getElementById("modalCallBtn")
const cancelBtn = document.querySelector(".btn-close")
const kakaoBtn = document.querySelector(".btn-kakao")
const todoId = document.querySelector(".share_idx").textContent

// 공유 버튼 클릭 시 공유하기 모달 표시
modalCallBtn.addEventListener("click", function (e) {
    console.log("modal invoke");
    shareModal.style.display = "flex";

    const url = DOMAIN + todoId

    $('input[name=url]').attr('value', url)
}, false)

// 취소 버튼 클릭 시 모달 숨기기
cancelBtn.addEventListener("click", function (e) {
    console.log("modal hide");
    shareModal.style.display = "none";
}, false)

// 복사하기
function copy_to_clipboard() {
    const copyText = document.getElementById("copyUrl");
    copyText.select();
    document.execCommand("Copy");
    alert("복사되었습니다")
}

