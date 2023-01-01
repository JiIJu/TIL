<template>
  <div>
    <HelloWorld
    :hello = 'hello'
    />
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld'
export default {
  name : 'FirstView',
  components: {
    HelloWorld,
  },
  computed:{
    hello() {
      return '첫 번째 페이지입니다.'
    }
  }
}
</script>

<style>

</style>