$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const app = Vue.createApp({
    delimiters: ["{", "}"],
    data() {
      return {
        userId: null,
        password: null,
      };
    },
    methods: {
      loginSubmit() {
        const data = {
          userId: this.userId,
          password: this.password,
        };

        $.ajax({
          type: "POST",
          url: "/account/login/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify(data),
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
            if (response.status == 1) {
              location.href = "/";
            } else {
              alert(response.msg);
            }
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      },
    },
  });

  app.mount("#loginDiv");
});
