$(() => {
  // https://it-eldorado.tistory.com/141
  // 장고 csrf 방지 매커니즘

  // https://docs.djangoproject.com/en/4.0/ref/csrf/
  // 장고 csrf 방지 레퍼런스

  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  // console.log(csrftoken);
  // console.log($("[name=csrfmiddlewaretoken]").val());

  // https://link2me.tistory.com/2103
  // 장고로 ajax 활용하기

  const app = Vue.createApp({
    data() {
      return {
        userId: null,
        password: null,
      };
    },
    methods: {
      signupSubmit() {
        // 정규식
        // https://blogpack.tistory.com/560
        // https://kkh0977.tistory.com/1099
        // https://basemenks.tistory.com/53

        const regId = /[^a-z|A-Z|0-9]/g;

        if (regId.test(this.userId)) {
          console.log(regId.test(this.userId));
          alert("아이디를 확인하여주세요. (영문자, 숫자만 가능)");
          return false;
        }

        const regPw = /[\s]/g;

        if (regPw.test(this.password)) {
          alert("비밀번호를 확인하여주세요. (공백 불가능)");
          return false;
        }

        const data = {
          userId: this.userId,
          password: this.password,
        };

        $.ajax({
          type: "POST",
          url: "/account/signup/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify(data),
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
            if (response.status == 1) {
              alert("가입이 완료되었습니다.");
              location.href = "/account/login/";
            } else if (response.status == 0) {
              alert("이미 있는 아이디입니다.");
            }
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      },
    },
  });

  app.mount("#signupDiv");
});
