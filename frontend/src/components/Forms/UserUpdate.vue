<template>
  <v-container id="user-profile" fluid tag="section">
    <br />
    <v-row justify="center">
      <v-col cols="12" md="8" style="background: #f9f9f9">
        <base-material-card>
          <template>
            <div
              class="text-start v-card--material__heading mb-n6 v-sheet theme--dark elevation-6 primary pa-7"
              style="width: 100%"
            >
              <div class="display-2 font-weight-light">Editar Perfil</div>

              <div class="subtitle-1 font-weight-light">Complete los datos</div>
            </div>
          </template>
          <br /><br />
          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field
                    :value="this.user.username"
                    class="purple-input"
                    label="Nombre de usuario"
                  />
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field
                    label="Email"
                    class="purple-input"
                    :value="this.user.email"
                  />
                </v-col>

                <v-col cols="12" md="6">
                  <v-text-field
                    label="Nombre"
                    class="purple-input"
                    :value="this.user.first_name"
                  />
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field
                    :value="this.user.last_name"
                    label="Apellido"
                    class="purple-input"
                  />
                </v-col>

                <div>
                  <v-menu
                    ref="menu"
                    v-model="menuBirth"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="dateBirth"
                        label="Fecha de nacimiento"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="dateBirth"
                      :active-picker.sync="activePickerBirth"
                      :max="new Date().toISOString().substr(0, 10)"
                      min="1950-01-01"
                      @change="save"
                    ></v-date-picker>
                  </v-menu>
                </div>
                <div>
                  <v-menu
                    ref="menu"
                    v-model="menuStart"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="dateStart"
                        label="Fecha de nacimiento"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="dateStart"
                      :active-picker.sync="activePickerStart"
                      :max="new Date().toISOString().substr(0, 10)"
                      min="1950-01-01"
                      @change="saveStart"
                    ></v-date-picker>
                  </v-menu>
                </div>
                <v-col cols="12" md="4">
                  <v-checkbox
                    :value="this.user.pay_last_month"
                    label="Al día"
                    class="purple-input"
                    color="primary"
                  />
                </v-col>

                <v-col cols="12">
                  <v-textarea
                    class="purple-input"
                    :value="this.user.observations"
                    disabled
                    label="Observaciones"
                  />
                </v-col>

                <v-col cols="12" class="text-right">
                  <v-btn color="primary" class="mr-0"> Update Profile </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import axios from "axios";
export default {
  name: "UserUpdate",

  created() {
    axios
      .get("http://localhost:8000/users/" + this.$session.get("user").id)
      .then((response) => {
        this.user = response.data[0];
        this.dateBirth = this.user.date_of_birth;
        this.dateStart = this.user.date_of_started;
        console.log(this.user);
      });
  },

  data: () => ({
    user: {},
    activePickerBirth: null,
    dateBirth: null,
    menuBirth: false,
    activePickerStart: null,
    dateStart: null,
    menuStart: false,
  }),
  watch: {
    menuBirth(val) {
      val && setTimeout(() => (this.activePickerBirth = "YEAR"));
    },
    menuStart(val) {
      val && setTimeout(() => (this.activePickerStart = "YEAR"));
    },
  },
  methods: {
    save(date) {
      this.$refs.menuBirth.save(date);
    },
    saveStart(date) {
      this.$refs.menuStart.save(date);
    },
  },
};
</script>
