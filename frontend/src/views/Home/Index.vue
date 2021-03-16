<template>
  <v-container>
    <NavBar />
    <div id="triangle-topleft"></div>
    <Carousel />
    <Presentation />
  </v-container>
</template>

<script>
import Carousel from "./Carousel";
import NavBar from "./NavBar";
import Presentation from "./Presentation";
export default {
  name: "Home",

  components: {
    NavBar,
    Presentation,
    Carousel,
  },

  data: () => ({}),
};
</script>
<style>
#triangle-topleft {
  width: 100%;
  height: 20em;
  background-color: #172b4d;
  border-radius: 0% 0% 80% 0%;
  position: absolute;
}
</style>