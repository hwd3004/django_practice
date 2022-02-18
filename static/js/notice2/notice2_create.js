$(() => {
  const app = Vue.createApp({
    delimiters: ["{", "}"],
    data() {
      return {
        data: {
          visibility: "공개",
          password: "",
        },
        code: {
          visibility: [
            {
              label: "공개",
              value: "공개",
            },
            {
              label: "비공개",
              value: "비공개",
            },
          ],
          password: "",
        },
      };
    },
    watch: {
      "data.visibility": {
        immediate: true,
        handler(value) {
          console.log("data.visibility : ", value);
        },
      },
      "data.password": {
        immediate: true,
        handler(value) {
          console.log("data.password : ", value);
        },
      },
      inputs: {
        deep: true,
        handler(value) {
          console.log(value);
        },
      },
      // https://thewebdev.info/2021/03/28/how-to-properly-watch-for-nested-data-in-vue-js-3-components/
      "inputs.visibility": {
        handler(value) {
          if (value == "공개") {
            $("#passwordLabel").hide();
            this.inputs.password = "";
          } else {
            $("#passwordLabel").show();
          }
        },
      },
    },
    methods: {
      // https://yiunsr.tistory.com/844 - vue.js 을 이용한 file 업로드 input
      setAttachment: function (event) {
        console.log(event.target.files[0].name);
      },
    },
  });

  app.component("code-radio", nn.vue.radio);

  app.mount("#app");

  $("#form").submit(function (e) {
    e.preventDefault();
    const formdata = new FormData(this);

    const textbox = document.querySelector(".note-editable").innerHTML;
    formdata.append("content", textbox);

    console.log(formdata.get("title"));

    // console.log("formdata : ", formdata);

    $.ajax({
      url: window.location.pathname,
      type: "POST",
      data: formdata,
      cache: false,
      contentType: false,
      processData: false,
      success: (response) => {
        console.log(response);
      },
      error: (error) => {
        alert("에러");
        console.log(error);
      },
    });
  });
});
