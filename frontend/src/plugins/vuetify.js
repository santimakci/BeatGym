import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import '@/sass/overrides.sass'

Vue.use(Vuetify);

export default new Vuetify({
      theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: '#09151E',
        secondary: '#aa66cc',
        accent: '#81d4fa',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107',
        anchor: '#ffffff'
      },
    },
  },
});
