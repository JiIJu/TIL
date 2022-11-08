<template>
  <div>
    <h1>주문 내역</h1>
    <h3>총 {{totalOrderCount}}건 : {{ totalOrderPrice}}원</h3>
    <div><ul>
      <OrderListItem
    v-for="(order,index) in orderList" 
    :key ="index"
    :order="order"
    />
    </ul></div>
    
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components:{
    OrderListItem,
    },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },
    orderList() {
      console.log(this.$store.state.orderList)
      return this.$store.state.orderList
    },
    totalOrderCount() {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice() {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>