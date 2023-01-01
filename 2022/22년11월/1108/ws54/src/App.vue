<template>
  <div id="app">
    
    <h1 class="text">Coffee Order App</h1>
    <div  style="display:flex;">
    <div
    style="width:33%;">
    <MenuList
    class="text"
    />
    </div>
    <div
    style="width:33%;">
    <SizeList
    class="text"
    />
  </div>
  <div 
  style="width:33%;"
  class="text">
    <optionList
    style="width:100%;"
    />
  </div>
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
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
  methods : {
    order() {
      this.$store.dispatch('order')
      this.$store.dispatch('option')
      this.$store.dispatch('optionzero')
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
