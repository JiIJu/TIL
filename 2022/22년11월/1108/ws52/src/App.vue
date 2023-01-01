<template>
  <div id="app">
    
    <h1>Coffee Order App</h1>
    <div>
    
    <MenuList
    style="width:50%; float:left;"
    @click="pickMenu"
    />
    <SizeList
    style="width:50%;float:right;"
    />
    <!-- <OrderList/> -->
  </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
// import OrderList from '@/components/OrderList'


export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    // OrderList,
  },
  methods : {
    pickMenu() {
      return this.$store.dispatch('pickMenu',this.menu)
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
.shadow {
  box-shadow: 5px 5px 5px 5px #c0bfbf;
}

</style>
