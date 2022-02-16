$("#passwordLabel").hide();
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

$("form").submit(function (e) {
  e.preventDefault();
  const formdata = new FormData(this);

  console.log("formdata : ", formdata);

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

const app = Vue.createApp({
  delimiters: ["{", "}"],

  data() {
    return {
      inputs: {
        title: "",
        visibility: "공개",
        password: "",
        content: "",
        attachment: [],
      },
    };
  },
  watch: {
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
    onSubmit: function (event) {
      const formdata = new FormData($("form")[0]);

      console.log(formdata);

      $.ajax({
        url: window.location.pathname,
        type: "POST",
        cache: false,
        contetnType: false,
        processData: false,
        enctype: "multipart/form-data",
        data: formdata,
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

app.mount("#app");
