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
    delimiters: ["{", "}"],
    data() {
      return {
        userId: "",
        password: "",
        checkPassword: "",
        username: "",
        department: "",
        position: "",
        emailName: "",
        emailServer: "",
        phoneNumberFirst: "02",
        phoneNumberMiddle: "",
        phoneNumberLast: "",
        mobilePhoneNumberFirst: "010",
        mobilePhoneNumberMiddle: "",
        mobilePhoneNumberLast: "",
        resultCheckExistId: false,
        resultCheckPassword: 0,
      };
    },
    methods: {
      checkExistId() {
        // 영어/숫자만 가능, 특수문자/공백 제외
        const regId = /[^a-z|A-Z|0-9]/g;

        if (regId.test(this.userId)) {
          console.log(regId.test(this.userId));
          alert("아이디를 확인하여주세요. (영문자, 숫자만 가능)");
          this.userId = null;
          return false;
        }

        if (this.userId.length < 3) {
          alert("아이디를 3자 이상 입력해주세요");
          return false;
        }

        const data = {
          userId: this.userId,
        };

        $.ajax({
          type: "POST",
          url: "/account/checkid/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify(data),
          headers: { "X-CSRFToken": csrftoken },
          success: (response) => {
            console.log("response : ", response);
            alert(response.msg);
            if (response.status == 1) {
              this.resultCheckExistId = true;
            }
          },
          error: (error) => {
            console.log("error : ", error);
          },
        });
      }, // checkExistId()
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

        // 특수문자가 있으면 true, 없으면 false
        const regUsername = /[^\w\sㄱ-힣]|[\_]/g;
        if (regUsername.test(this.username)) {
          alert("성명을 확인하여주세요.");
          return false;
        }

        const regEmailName = /[^a-z|A-Z|0-9]/g;
        if (regEmailName.test(this.emailName)) {
          alert("이메일 이름을 확인하여주세요.");
          return false;
        }

        if (this.emailServer.length < 4) {
          alert("이메일 주소를 확인하여주세요");
          return false;
        }

        // 숫자 3,4자리만 가능, 통과하면 true, 걸리면 false
        const regPhoneNumber = /^[0-9_-]{3,4}$/;
        if (this.phoneNumberMiddle.length > 0 && this.phoneNumberLast.length > 0) {
          if (!regPhoneNumber.test(this.phoneNumberMiddle) || !regPhoneNumber.test(this.phoneNumberLast)) {
            alert("일반전화번호를 확인하여주세요.");
            return false;
          }
        }

        if (!regPhoneNumber.test(this.mobilePhoneNumberMiddle) || !regPhoneNumber.test(this.mobilePhoneNumberLast)) {
          alert("휴대전화번호를 확인하여주세요.");
          return false;
        }

        const data = {
          userId: this.userId,
          password: this.password,
          username: this.username,
          department: this.department,
          position: this.position,
          email: `${this.emailName}@${this.emailServer}`,
          phoneNumber: `${this.phoneNumberFirst}-${this.phoneNumberMiddle}-${this.phoneNumberLast}`,
          mobilePhoneNumber: `${this.mobilePhoneNumberFirst}-${this.mobilePhoneNumberMiddle}-${this.mobilePhoneNumberLast}`,
        };

        if (this.resultCheckExistId && this.resultCheckPassword == 2) {
          $.ajax({
            type: "POST",
            url: "/account/signup/",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify(data),
            headers: { "X-CSRFToken": csrftoken },
            success: (response) => {
              console.log("response : ", response);
              alert(response.msg);
              if (response.status == 1) {
                location.href = "/account/login";
              }
            },
            error: (error) => {
              console.log("error : ", error);
            },
          });
        } else if (!this.resultCheckExistId) {
          alert("아이디를 확인해주세요.");
        } else if (!this.resultCheckPassword) {
          alert("비밀번호를 확인해주세요.");
        }
      }, // signupSubmit()
      onChangeCheckExistId(event) {
        resultCheckExistId = false;
      },
      onChangeCheckPassword(event) {
        if (this.password != this.checkPassword) {
          alert("비밀번호를 확인하여주세요.");
          this.checkPassword = null;
          $("#checkPassword").focus();
          this.resultCheckPassword = 1;
          return false;
        } else {
          this.resultCheckPassword = 2;
        }
      },
    },
  });

  app.mount("#signupDiv");
});
