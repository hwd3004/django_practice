const nn = {};
nn.vue = {};

nn.vue.radio = {
  data() {
    return {
      currentVisibility: this.visibility,
      currentPassword: this.password,
    };
  },
  template: `
      <div>
        <span>공개여부</span>
        &nbsp;
        <span v-for="row in code">
          <label>
            <span>{{row.label}}</span>
            <input type="radio" name="visibility" v-model="currentVisibility" :value="row.value" />
          </label>
          &nbsp;
        </span>
        <label id="passwordLabel">
          <span>비밀번호</span>
          <input type="password" name="password" v-model="currentPassword"/>
        </label>
      </div>
      `,
  props: ["code", "visibility", "password"],
  watch: {
    currentVisibility: {
      immediate: true,
      handler(value) {
        console.log("currentVisibility : ", value);
        this.$emit("update:visibility", value);

        setTimeout(() => {
          const passwordLabel = document.querySelector("#passwordLabel");
          if (value == "공개") {
            passwordLabel.style["display"] = "none";
            this.currentPassword = "";
          } else {
            passwordLabel.style["display"] = "inline-block";
          }
        }, 0);
      },
    },
    currentPassword: {
      immediate: true,
      handler(value) {
        console.log("currentPassword : ", value);
        this.$emit("update:password", value);
      },
    },
  },
};
