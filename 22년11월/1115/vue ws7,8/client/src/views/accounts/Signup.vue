<template>
  <div>
    <span>사용자 이름 : <input type="text" v-model='username'></span> <br>
    <span>비밀번호 : <input type="text" v-model='password'></span> <br>
    <span>비밀번호 확인 : <input type="text" v-model='passwordConfirm'></span><br>
    <span>이메일 : <input type="text" v-model='email'></span><br>
    <button @click='signup'>Sign Up</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      username : null,
      password : null,
      passwordConfirm : null,
      email : null,
    }
  },
  methods: {
    signup: function () {
      axios({
        method : 'post',
        url : `http://127.0.0.1:8000/accounts/signup/`,
        data : {
          username : this.username,
          password : this.password,
          passwordConfirm : this.password,
          email : this.email,
        }
      })
      .then((res)=> {
        console.log(res)
        this.$router.push({name : 'Login'})
      })
      .catch((err) => {
        console.log(err)
        console.log(1234)
      })
    }
  }
}
</script>


<style>


</style>