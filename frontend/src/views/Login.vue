<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <b-form ref="loginForm" v-model="valid" lazy-validation>
            <b-form-input
              v-model="user.email"
              :rules="loginEmailRules"
              label="E-mail"
              required
            ></b-form-input>

            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="user.password"
            >
            </base-input>

            <div class="text-center">
              <base-button @click="login" type="primary" class="my-4"
                >Iniciar Sesión</base-button
              >
            </div>
          </b-form>
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

  data: () => ({
    user: {
      email: "",
      password: "",
    },
    loginEmailRules: [
      (v) => !!v || "Required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),

  methods: {
    login() {
      console.log(this.user.email);
      axios
        .post("http://localhost:8000/users/login/", this.user)
        .then((response) => {
          console.log(response);
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
