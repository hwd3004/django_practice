$(() => {
  const checkPassword = document.querySelector("#checkPassword");
  const checkVisibility = document.querySelector("#checkVisibility");

  let notice_detail = document.querySelector("#notice_detail");

  if (checkVisibility.value == "public") {
    notice_detail.style["display"] = "block";
  } else {
    const result = prompt("비밀번호를 입력하세요");

    if (result == checkPassword.value) {
      notice_detail.style["display"] = "block";
    } else {
      alert("비밀번호가 틀렸습니다.");
      location.href = "/notice_list/";
    }
  }


  // if (checkVisibility.value == "private") {
  //   notice_detail.style["display"] = "none";

  //   setTimeout(() => {
  //     const result = prompt("비밀번호를 입력하세요");

  //     if (result == checkPassword.value) {
  //       notice_detail.style["display"] = "block";
  //     } else {
  //       alert("비밀번호가 틀렸습니다.");
  //       location.href = "/notice_list/";
  //     }
  //   }, 0);
  //   // https://ko.javascript.info/settimeout-setinterval
  //   // 대기 시간이 0인 setTimeout
  //   // 대기 시간을 0으로 설정하면 func을 ‘가능한 한’ 빨리 실행할 수 있습니다.
  //   // 다만, 이때 스케줄러는 현재 실행 중인 스크립트의 처리가 종료된 이후에 스케줄링한 함수를 실행합니다.
  // }
});
