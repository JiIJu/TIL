<template>
  <div id="app">
    
    <h1 class="text">Coffee Order App</h1>
    <div >
    <MenuList
    style="width:50%; float:left;"
    class="text"
    />
    </div>
    <div>
    <SizeList
    style="width:50%;float:right;"
    class="text"
    />
  </div>
  <OrderList/>
  <div>
    <button 
    style="width: 100%;padding: 2px;%"
    @click="order"
    >장바구니</button>
    
  </div>
  
  </div>
  
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'


export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    OrderList,
  },
  methods : {
    order() {
      this.$store.dispatch('order')
    }
    
  },
  computed: {
    // totalOrderCount() {
    //   return this.$store.getters.totalOrderCount
    // },
    // totalOrderPrice() {
    //   return this.$store.getters.totalOrderPrice
    // }
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
.text {
  text-align: center;
}

</style>
