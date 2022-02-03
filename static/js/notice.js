$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const app = Vue.createApp({
    delimiters: ["{", "}"],
    methods: {
      noticeSubmit() {
        const formData = new FormData($("#form")[0]);

        $.ajax({
          type: "POST",
          url: "/notice_newpost/",
          // dataType: "json",
          cache: false,
          contetnType: false, // false 로 선언 시 content-type 헤더가 multipart/form-data로 전송되게 함
          processData: false, // false로 선언 시 formData를 string으로 변환하지 않음
          enctype: "multipart/form-data",
          data: formData,
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      },
    },
  });

  app.mount("#noticeNewpostDiv");
});
