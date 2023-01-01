<template>
  <div>
    <span>사용자 이름 : <input type="text" v-model='username'></span> <br>
    <span>비밀번호 : <input type="text" v-model='password'></span> <br>
    <button @click="login">login</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    login: function () {
      const credentials = {
        username : this.username,
        password : this.password,
      }
      axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/api/token/',
        data : credentials,
      })
      .then((res) => {
        localStorage.setItem('jwt',res.data.access);
        this.$emit('login');
        this.$router.push({name:'TodoList'})
      })
    }
  }
}
</script>
