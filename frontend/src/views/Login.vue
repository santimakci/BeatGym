<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <form role="form">
            <base-input
              v-on:input="updateEmail($event.target.value)"
              formClasses="input-group-alternative mb-3"
              addon-left-icon="ni ni-email-83"
              :rules="loginEmailRules"
              placeholder="E-mail"
              focused
            ></base-input>
            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-on:input="updatePass($event.target.value)"
            >
            </base-input>

            <div class="text-center">
              <base-button @click="login" type="primary" class="my-4"
                >Iniciar Sesión</base-button
              >
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <a href="/" class="text-light"><small>Inicio</small></a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "login",

  data() {
    return {
      user: {
        email: "",
        password: "",
      },
    };
  },

  methods: {
    updateEmail(evt) {
      this.user.email = evt;
    },
    updatePass(evt) {
      this.user.password = evt;
    },
    login() {
      console.log(this.user);
      axios
        .post("http://localhost:8000/users/login/", this.user)
        .then((response) => {
          console.log(response);
          if (response.status === 201 && "access_token" in response.data) {
            debugger;
            this.$session.start();
            this.$session.set("jwt", response.data.access_token);
            this.$session.set("user", response.data.user);
            this.$router.push("/");
          }
        });
    },
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => (v && v.length >= 8) || "Min 8 characters",
    },
  },
};
</script>
<style></style>
