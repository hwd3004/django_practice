$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const app = Vue.createApp({
    delimiters: ["{", "}"],
    data() {
      return {
        userId: null,
        username: null,
        email: null,
      };
    },
    methods: {
      findidSubmit() {
        const data = {
          username: this.username,
          email: this.email,
          reqType: "findid",
        };

        $.ajax({
          type: "POST",
          url: "/account/findid/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify(data),
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
            if (response.status == 1) {
            } else if (response.status == 0) {
            }
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      },
      findpasswordSubmit() {
        const data = {
          userId: this.userId,
          username: this.username,
          email: this.email,
          reqType: "findpassword",
        };

        $.ajax({
          type: "POST",
          url: "/account/findid/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify(data),
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
            if (response.status == 1) {
            } else if (response.status == 0) {
            }
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      },
    },
  });

  app.mount("#findidDiv");
});
