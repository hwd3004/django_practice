$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const visibility = document.querySelectorAll("[name=visibility]");

  const passwordLabel = document.querySelector("#passwordLabel");
  const password = document.querySelector("[name=password");

  const addAttach = document.querySelector("#addAttach");
  const removeAttach = document.querySelector("#removeAttach");

  const attachBox = document.querySelector("#attachBox");

  // https://meanbymin.tistory.com/78
  // http://www.w3big.com/ko/jsref/met-node-removechild.html

  addAttach.addEventListener("click", function () {
    const newInputAttach = document.createElement("input");
    newInputAttach.type = "file";
    newInputAttach.name = "attachment";
    attachBox.appendChild(newInputAttach);
  });

  removeAttach.addEventListener("click", function () {
    console.log(attachBox.childNodes);
    console.log(attachBox.childNodes.length);
    if (attachBox.childNodes.length > 3) {
      attachBox.removeChild(attachBox.childNodes[attachBox.childNodes.length - 1]);
    } else {
      const attach = document.querySelector("[name=attachment]");
      console.log(attach.value);
      attach.value = null;
    }
  });

  for (let index = 0; index < visibility.length; index++) {
    visibility[index].addEventListener("click", function () {
      console.log(this.value);

      if (this.value == "private") {
        passwordLabel.style["display"] = "inline-block";
      } else {
        passwordLabel.style["display"] = "none";
        password.value = null;
      }
    });
  }

  $("#form").submit(function (e) {
    e.preventDefault();
    const formdata = new FormData(this);
    console.log(formdata);

    const thisform = $(this);
    console.log(thisform);

    $.ajax({
      url: window.location.pathname,
      type: "POST",
      data: formdata,
      cache: false,
      contentType: false,
      processData: false,
      xhr: () => {
        // https://youtu.be/osqkFdIyDNg
        // https://myhappyman.tistory.com/178
        const xhr = $.ajaxSettings.xhr();

        xhr.upload.onprogress = (ev) => {
          const percentage = ((ev.loaded / ev.total) * 100) | 0;
          document.getElementById("progress_div").style["display"] = "block";
          document.getElementById("progress_bar").style["width"] = "" + percentage + "%";
          document.getElementById("progress_bar").innerHTML = "" + percentage + "%";
          document.getElementById("progress_text").innerHTML =
            "Uploaded : " + parseInt(ev.loaded / 1000000) + "/" + parseInt(ev.total / 1000000) + " MB";
          console.log("Uploaded : " + ev.loaded);
          console.log("TOTAL : " + ev.total);

          console.log(percentage);
        };

        return xhr;
      },
      success: (response) => {
        console.log(response);
        if (response.status != 1) {
          alert(response.msg);
        }
      },
      error: (error) => {
        alert("에러");
        console.log(error);
      },
    });
  });

  // const app = Vue.createApp({
  //   delimiters: ["{", "}"],
  //   methods: {
  //     noticeSubmit() {
  //       const formData = new FormData($("#form")[0]);

  //       console.log(formData);

  //       $.ajax({
  //         type: "POST",
  //         url: "/notice_newpost/",
  //         // dataType: "json",
  //         cache: false,
  //         contetnType: false, // false 로 선언 시 content-type 헤더가 multipart/form-data로 전송되게 함
  //         processData: false, // false로 선언 시 formData를 string으로 변환하지 않음
  //         enctype: "multipart/form-data",
  //         data: formData,
  //         headers: { "X-CSRFToken": csrftoken },
  //         success: (response) => {
  //           console.log("response : ", response);
  //         },
  //         error: (error) => {
  //           console.log("error : ", error);
  //         },
  //       });
  //     },
  //   },
  // });

  // app.mount("#noticeNewpostDiv");
});
