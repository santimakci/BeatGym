<template>
  <v-app-bar app color="primary" dark>
    <div class="d-flex align-center" style="margin-left: auto">
      <v-row justify="center">
        <v-btn
          v-if="
            this.$session.exists() &&
            this.$session.get('user').is_teacher == true
          "
          icon
        >
          <v-icon>mdi-account-plus-outline</v-icon>
        </v-btn>
        <v-menu left bottom>
          <template
            v-if="this.$session.exists()"
            v-slot:activator="{ on, attrs }"
          >
            <v-btn icon v-bind="attrs" v-on="on">
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item>
              <v-list-item-title v-if="this.$session.exists()">{{
                this.$session.get("user").username
              }}</v-list-item-title>
            </v-list-item>
            <v-list-item v-for="n in actions" :key="n.id" :to="n.to">
              <v-list-item-title>{{ n.title }}</v-list-item-title>
            </v-list-item>
            <hr />
            <v-list-item type="submit" @click="logout">
              <v-list-item-title>Cerrar Sesion</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu></v-row
      >
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: "NavBar",
  props: {},
  methods: {
    logout() {
      console.log(this.$session.getAll());
      this.$session.destroy();
      this.$router.push("/");
      this.$forceUpdate();
    },
  },

  created() {
    this.urlProfile = "/profile/" + this.$session.get("user").id;
    this.actions[0].to = this.urlProfile;
  },

  data: () => ({
    user: {},
    actions: [
      {
        id: 0,
        title: "Perfil",
        to: "",
      },
    ],
  }),
};
</script>
