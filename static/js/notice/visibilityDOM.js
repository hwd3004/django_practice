$(() => {
  const visibility = document.querySelectorAll("[name=visibility]");

  const passwordLabel = document.querySelector("#passwordLabel");
  const password = document.querySelector("[name=password]");

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
});
