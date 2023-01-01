<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{name : 'home'}">집으로!</router-link>
    <button @click="toHome">홈으로</button>
    <input type="text" @keyup.enter="goHello" v-model="hellotext">
  </div>
</template>


<script>
export default {
  name : 'AboutView',
  methods: {
    toHome() {
      this.$router.push({ name : 'home'})
    },
    goHello() {
      this.$router.push({name:'hello' , params:{userName : this.hellotext}})
    }
  },
  data()  {
    return {
      hellotext : null,
    }
  },


}
</script>