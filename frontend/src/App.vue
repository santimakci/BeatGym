<template>
  <v-app>
    <v-main>
      <NavBar :key="$route.fullPath" />
      <router-view />
      <Drawer v-if="this.$session.exists()" />
    </v-main>
  </v-app>
</template>

<script>
import NavBar from "./components/NavBar";
import Drawer from "./components/Drawer";
export default {
  name: "App",

  components: {
    NavBar,
    Drawer,
  },
  created() {
    this.currentTitle = this.$router.history.current.name;
    if (!this.$session.exists()) {
      this.$router.push("/");
    }
  },

  data: () => ({
    currentTitle: "",
  }),
};
</script>
<style>
@import "./assets/styles/general.css";
</style>