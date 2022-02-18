$(() => {
  $.ajax({
    url: "/notice2_getList/",
    type: "GET",
    success: (response) => {
      console.log(response);
    },
    error: (error) => {
      alert("에러");
      console.log(error);
    },
  });
});
