<template>
  <li>
    <div style="display:flex;margin:20px;">
      <img :src="order.menu.image" style="height:50px;width:50px;float:left;">
      <span style="width:100%;">
        메뉴 : {{order.menu.name}}
        <br>
        사이즈 : {{order.size.name}} 
        <span style="float:right;">{{order.menu.price}} 원</span>
      </span>
    </div>
    
    <hr>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    // totalPrice: function () {
    // },
  },
  method: {
    
  }
}
</script>

<style>
</style>