<template>
  <v-container style="background: #eee">
    <UserUpdate />
  </v-container>
</template>


<script>
import UserUpdate from "./Forms/UserUpdate";

export default {
  components: { UserUpdate },
  name: "Profile",
  comments: {
    UserUpdate,
  },

  data: () => ({}),
};
</script>
