import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPageView from '../views/AllTodoPageView.vue'
import TodayTodoPageView from '../views/TodayTodoPageView.vue'
import ImportantTodoPageView from '../views/ImportantTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllTodoPage',
    component: AllTodoPageView
  },
  {
    path: '/today',
    name: 'TodayTodoPage',
    component: TodayTodoPageView
  },
  {
    path: '/important',
    name: 'importantTodoPage',
    component: ImportantTodoPageView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
