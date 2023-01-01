<template>
  <div>
    <h1>중요 할일</h1>
    <div  v-for="(todo,index) in todoList" :key="index">
      <div class="important" v-if="todo.isImportant">
        <div style="margin:5px;float:left;">
      <button style="background-color:rgba(0,0,0,0); border: 0px;" v-if="todo.isCompleted" @click="completed(todo)"><i class="bi bi-check-square-fill"></i></button>
    <button style="background-color:rgba(0,0,0,0); border: 0px;" @click="completed(todo)" v-else ><i class="bi bi-check-square"></i></button>
    </div>
    {{todo.content}}
  <div style="float:right;">
    <button style="background-color:rgba(0,0,0,0); border: 0px;" v-if="todo.isImportant" @click="important(todo)"><i class="bi bi-star-fill" ></i></button>
    <button style="background-color:rgba(0,0,0,0); border: 0px;" @click="important(todo)" v-else ><i class="bi bi-star"></i></button>
  </div>
</div>
  </div>
  
  </div>
</template>

<script>
export default {
  name : 'ImportantTodoPage',
  
  data() {
    return {
    }
  },

  computed: {
    todoList() {
      return this.$store.state.todos.list;
    },
  },
  methods : {
    completed(todos) {
      todos.isCompleted = !todos.isCompleted
    },
    important(todos) {
      // console.log(todos)
      todos.isImportant = !todos.isImportant
      // this.isImportant = !this.isImportant
    },
    createTodo() {
      const content = this.content
      
      this.$store.dispatch('createTodo',content)
      this.content = null
      // this.$store.state.list.push()
    }
  }
}
</script>

<style>

</style>