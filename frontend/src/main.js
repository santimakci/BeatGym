import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import VueSession from 'vue-session'


Vue.config.productionTip = false

var options = {
    persist: true
}
Vue.use(VueSession, options)


new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
