<template>
  <base-nav
    class="navbar navbar-horizontal navbar-expand-lg navbar-dark bg-default"
  >
    <template v-slot:brand>
      <a class="navbar-brand" href="#"> LOGO </a>
    </template>
    <template v-slot:scope="{ closeMenu }">
      <div class="navbar-collapse-header">
        <div class="row">
          <div class="col-6 collapse-brand">
            <a href="../../index.html">
              <img src="/img/brand/blue.png" />
            </a>
          </div>
          <div class="col-6 collapse-close">
            <button
              @click="closeMenu"
              type="button"
              class="navbar-toggler"
              data-toggle="collapse"
              data-target="#navbar-default"
              aria-controls="navbar-default"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span></span>
              <span></span>
            </button>
          </div>
        </div>
      </div>
    </template>

    <ul class="navbar-nav ml-lg-auto">
      <li class="nav-item dropdown">
        <a
          class="nav-link nav-link-icon"
          href="/login"
          id="navbar-default_dropdown_1"
          role="button"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <i class="ni ni-single-02"></i>
          <span class="nav-link-inner--text d-lg-none">Ingresar</span>
        </a>
        <div
          class="dropdown-menu dropdown-menu-right"
          aria-labelledby="navbar-default_dropdown_1"
        >
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
  </base-nav>
</template>
<script>
export default {
  name: "NavBar",

  data: () => ({}),

  created() {},
  methods: {
    logout() {
      /* console.log(this.$session.getAll());
      this.$session.destroy();
      this.$router.push("/");
      this.$forceUpdate(); */
    },
  },
};
</script>