$(() => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const addAttach = document.querySelector("#addAttach");
  const removeAttach = document.querySelector("#removeAttach");

  const attachBox = document.querySelector("#attachBox");

  const hasAttach = document.querySelectorAll(".hasAttach");

  const removeHasAttach = document.querySelectorAll(".removeHasAttach");

  for (let index = 0; index < removeHasAttach.length; index++) {
    removeHasAttach[index].addEventListener("click", function () {
      const res = confirm("첨부파일을 삭제하시겠습니까? 허용하시면 지금 즉시 삭제됩니다.");

      if (res) {
        const hasAttachId = parseInt(hasAttach[index].value);

        $.ajax({
          url: "/notice_removeHasAttach/",
          type: "POST",
          data: JSON.stringify({ hasAttachId: hasAttachId }),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log(response);
            if (response.status != 1) {
              alert(response.msg);
            }

            if (response.status == 1) {
              this.parentNode.remove();
            }
          },
          error: (error) => {
            alert("에러");
            console.log(error);
          },
        });
      }
    });
  }

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

  $("#form").submit(function (e) {
    e.preventDefault();
    const formdata = new FormData(this);

    // if (hasAttach) {
    //   for (let index = 0; index < hasAttach.length; index++) {
    //     const id = parseInt(hasAttach[index].value);
    //     console.log(typeof id);
    //     formdata.append("hasAttach", id);
    //   }
    // }

    console.log("formdata : ", formdata);

    // const thisform = $(this);
    // console.log(thisform);

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
