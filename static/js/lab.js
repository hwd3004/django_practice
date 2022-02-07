// https://learnbatta.com/blog/django-image-and-file-upload-using-ajax-21/
$(() => {
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
        $(".error").remove();
        console.log(response);
        if (response.errors) {
          $.each(response.errors, (name, error) => {
            console.log(name);
            console.log(error);
            error = '<small class="text-muted error">' + error + "</small>";
            thisform.find(`[name=${name}]`).after(error);
          });
        }
      },
      error: (error) => {
        alert("에러");
        console.log(error);
      },
    });
  });
});
