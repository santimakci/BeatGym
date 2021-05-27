<template>
  <div id="app">
    <v-app>
      <v-card class="mx-auto my-12 px-4" max-width="600">
        <v-alert v-if="badRequest" type="error"
          >Nombre de usuario o contraseña incorrectos</v-alert
        >
        <v-card-text>
          <v-form ref="loginForm" v-model="valid" lazy-validation>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="user.email"
                  :rules="loginEmailRules"
                  label="E-mail"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="user.password"
                  :append-icon="show1 ? 'eye' : 'eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  name="input-10-1"
                  label="Password"
                  hint="At least 8 characters"
                  counter
                  @click:append="show1 = !show1"
                ></v-text-field>
              </v-col>
              <v-spacer></v-spacer>
              <v-col
                class="d-flex"
                style="margin: auto"
                cols="8"
                sm="3"
                xsm="12"
                align-end
              >
                <v-btn
                  x-large
                  block
                  center
                  :disabled="!valid"
                  color="primary"
                  @click="validate"
                >
                  Iniciar sesión
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-app>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Login",
  created() {
    if (this.$session.exists()) {
      this.$router.push("/dashboard");
    }
  },
  methods: {
    validate() {
      if (this.$refs.loginForm.validate()) {
        this.badRequest = false;
        axios
          .post("http://localhost:8000/users/login/", this.user)
          .then((response) => {
            console.log(response);
            if (response.status === 201 && "access_token" in response.data) {
              this.$session.start();
              this.$session.set("jwt", response.data.access_token);
              this.$session.set("user", response.data.user);
              console.log(response.data.user);
              this.$router.push("/dashboard");
            }
          })
          .catch(() => {
            this.badRequest = true;
            this.user.password = "";
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
  data: () => ({
    dialog: true,
    tab: 0,
    tabs: [{ name: "Login", icon: "mdi-account" }],
    valid: true,
    badRequest: false,
    user: {
      password: "",
      email: "",
    },
    loginEmailRules: [
      (v) => !!v || "Required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    emailRules: [
      (v) => !!v || "Required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],

    show1: false,
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => (v && v.length >= 8) || "Min 8 characters",
    },
  }),
};
</script>