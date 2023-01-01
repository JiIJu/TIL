<template>
  <div>
    <h1>로그아웃~~~~</h1>
    <button @click="logout">logout</button>
  </div>
</template>

<script>
export default {
    name : 'Logout',
    methods : {
    logout() {

      if (window.localStorage.getItem('jwt')) {
        window.localStorage.removeItem('jwt')
        this.$router.push({name:'TodoList'})
      } else {
        this.$router.push({name:'Login'})
      }
    }
    },
}
</script>

<style>

</style>