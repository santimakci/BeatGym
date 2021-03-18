import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import ArgonDashboard from "./plugins/argon-dashboard";
import "element-plus/lib/theme-chalk/index.css";
import VueSession from "vue-session";



/* let appInstance = createApp(App);

var options = {
    persist: true
}
appInstance.use(VueSession, options)
appInstance.use(router);
appInstance.use(ArgonDashboard);
appInstance.mount("#app"); */
debugger

Vue.config.productionTip = false

var options = {
    persist: true
}
Vue.use(VueSession, options)
Vue.use(ArgonDashboard);


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

