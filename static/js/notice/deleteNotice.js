$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const deleteNotice = document.querySelector("#deleteNotice");

  const noticeId = document.querySelector("#noticeId");

  deleteNotice.addEventListener("click", function () {
    const res = confirm("글을 삭제하시겠습니까? 첨부파일도 함께 삭제됩니다.");

    if (res) {
      $.ajax({
        url: `/notice_delete/${parseInt(noticeId.value)}/`,
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        headers: { "X-CSRFToken": csrftoken },
        success: (response) => {
          console.log(response);
          if (response.status != 1) {
            alert(response.msg);
          }

          if (response.status == 1) {
            location.href = "/notice_list/";
          }
        },
        error: (error) => {
          alert("에러");
          console.log(error);
        },
      });
    }
  });
});
