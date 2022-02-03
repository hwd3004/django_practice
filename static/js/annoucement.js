$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const app = Vue.createApp({
    delimiters: ["{", "}"],
    data() {
      return {
        title: "",
        author: "",
        visibility: "",
        content: "",
        file: null,
      };
    },
    methods: {
      addFileList() {
        console.log("asdsad");
      },
      removeFileList() {
        console.log("zxczxczxc");
      },
      annoucementSubmit() {
        // console.log(document.querySelector("#author").value);
        const author = document.querySelector("#author").value;

        // console.log($("input[type=file]"));
        // console.log($("input[type=file]").length);

        // const fileList = $("input[type=file]");

        // const data = {
        //   title: this.title,
        //   author,
        //   visibility: this.visibility,
        // };

        // let formData = new FormData();

        // for (let index = 0; index < fileList.length; index++) {
        //   if (fileList[index].files[0]) {
        //     formData.append("file", fileList[index].files[0]);
        //   }
        // }

        const formData = new FormData($("#form")[0]);
        console.log($("#form")[0]);

        // const formData = new FormData();
        // const title = this.title;
        // formData.append("title", title);

        // $.ajax({
        //   type: "POST",
        //   url: "/annoucement/newpost/",
        //   // dataType: "json",
        //   cache: false,
        //   contetnType: false, // false 로 선언 시 content-type 헤더가 multipart/form-data로 전송되게 함
        //   processData: false, // false로 선언 시 formData를 string으로 변환하지 않음
        //   enctype: "multipart/form-data",
        //   data: formData,
        //   headers: { "X-CSRFToken": csrftoken },
        //   success: (response) => {
        //     console.log("response : ", response);
        //   },
        //   error: (error) => {
        //     console.log("error : ", error);
        //   },
        // });

        $.ajax({
          type: "POST",
          url: "/annoucement/newpost2/",
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

  app.mount("#newpostDiv");
});
