import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../components/Dashboard'
import Login from '../components/Login'
import NotFound from '../components/Errors/NotFound'
import Profile from '../components/Profile'


Vue.use(VueRouter)

const routes = [

      {
        path: '/',
        name: 'Login',
        component: Login
      },
      {
          path: '/dashboard',
          name: 'Dashboard',
          component: Dashboard
      },
      {
          path: '/profile/:id',
          name: 'Profile',
          component: Profile
      },
      {
          path: '*',
          name: 'Not Found',
          component: NotFound,
      }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router