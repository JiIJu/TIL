import Vue from 'vue'
import Vuex from 'vuex'
import todos from "./modules/todos.js"
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    nowDateObj : new Date()
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state,todo) {
      console.log(todo)
      state.todos.list.push(todo)
    }
  },
  actions: {
    createTodo(context,data) {
      console.log(context)
      if (data){
      const year = this.state.nowDateObj.getFullYear()
      const month = this.state.nowDateObj.getMonth()
      const date = this.state.nowDateObj.getDate()
      const todo = {
        id : this.state.nowDateObj.getTime(),
        content : data,
        dueDateTime : `${year}-${month+1}-${date+1}T00:00` ,
        isCompleted:false,
        ifImportant : false
      }
      context.commit('CREATE_TODO',todo)}
    }
  },
  modules: {
    todos,
  }
})
