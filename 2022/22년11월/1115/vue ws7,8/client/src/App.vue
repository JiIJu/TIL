<template>
  <div id="app">
    <div id="nav">
      <span>
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
      </span>
      <span>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }"
        
        >Login</router-link> |
        <router-link :to="{name:'Logout'}" v-if="is_login">Logout</router-link>
      </span>
      
    </div>
    <router-view @login="login"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      is_login : false,
    }
  },
  methods: {
    login: function () {
      this.is_login = true
      console.log(this.is_login)
    },
    
  },
  created() {
    if (window.localStorage.getItem('jwt')) {
      this.is_login=true
    }
    else {
    this.is_login = false
  }
    
    console.log(this.is_login)
  }
  
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
