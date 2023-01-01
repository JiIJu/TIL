import Vue from 'vue'
import VueRouter from 'vue-router'

// import LottoView from '@/views/LottoView'
import LunchView from '@/views/LunchView'
Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/lotto/6',
  //   name: 'lotto',
  //   component: LottoView
  // },
  {
    path: '/lunch',
    name: 'lunch',
    component : LunchView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
