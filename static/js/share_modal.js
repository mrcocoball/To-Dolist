
const DOMAIN = 'http://todolist.ykstyle.info:8083/'

// 모달 관련 변수
const shareModal = document.getElementById("shareModal")
const modalCallBtn = document.getElementById("modalCallBtn")
const cancelBtn = document.querySelector(".btn-close")
const kakaoBtn = document.getElementById("kakaoShareBtn")
const todoId = document.querySelector(".share_idx").textContent
const shareLocation = document.querySelector(".share_location").textContent

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
    document.execCommand("Copy"); // deprecated 되었으나 clipboard.js까지 깔아가면서 할 필요는 없을 것 같음
    alert("복사되었습니다")
}


// 카카오톡 공유 버튼 클릭 시
kakaoBtn.addEventListener("click", function (e) {
    console.log("kakao share invoke")

    if (shareLocation == 'profiles') {

        const userRank = document.querySelector(".user_rank").textContent

        Kakao.Share.sendCustom({
            templateId: 91666,
            templateArgs: {
              title: '당신 계획력 랭크 티어가?',
              description: '저의 티어는 ' + userRank + ' 입니다만?',
              url : todoId
            },
        });
    }

    if (shareLocation == 'todos') {
        Kakao.Share.sendCustom({
            templateId: 91670,
            templateArgs: {
              title: '계획을 공유해드립니다',
              description: '멋진 계획을 같이 확인해볼까요?',
              url : todoId
            },
        });
    }

}, false)
