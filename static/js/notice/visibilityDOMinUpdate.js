$(() => {
  const visibilityValue = document.querySelector("#visibilityValue");
  const passwordValue = document.querySelector("#passwordValue");

  const visibility = document.querySelectorAll("[name=visibility]");

  const passwordLabel = document.querySelector("#passwordLabel");
  const password = document.querySelector("[name=password]");
  
  if (visibilityValue.value == "public") {
    visibility[0].checked = true;
  } else {
    visibility[1].checked = true;
    passwordLabel.style["display"] = "inline-block";
    password.value = passwordValue.value;
  }
  
  for (let index = 0; index < visibility.length; index++) {
    visibility[index].addEventListener("click", function () {
      console.log(this.value);

      if (this.value == "private") {
        passwordLabel.style["display"] = "inline-block";
      } else {
        passwordLabel.style["display"] = "none";
        password.value = passwordValue.value;
      }
    });
  }
});
