<template>
  <!-- Add expand-on-hover to v-navigation-drawer to hover the drawer -->
  <div id="app">
    <v-navigation-drawer color="primary" permanent app>
      <v-divider></v-divider>
      <v-img
        alt="Vuetify Logo"
        class="shrink mr-2"
        contain
        style="margin: 10px"
        src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
        transition="scale-transition"
        width="30"
      />

      <v-list nav dense>
        <v-list-item v-for="item in items" :key="item.id" :to="item.to">
          <v-list-item-icon>
            <v-icon color="white" small>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="title white--text">{{
            item.title
          }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
/* import NavBar from "./components/NavBar";
 */ /* import Drawer from "./components/Drawer"; */
export default {
  name: "Drawer",
  data: () => ({
    items: [
      {
        id: 1,
        icon: "mdi-view-dashboard",
        title: "Inicio",
        to: "/",
      },
      {
        id: 2,
        icon: "mdi-account",
        title: "Perfil",
        to: "/profile",
      },
      {
        title: "Planes",
        id: 3,
        icon: "mdi-clipboard-outline",
        to: "/tables/regular-tables",
      },
      {
        title: "Estadísticas",
        id: 4,
        icon: "mdi-format-font",
        to: "/components/typography",
      },
    ],
  }),
};
</script>
