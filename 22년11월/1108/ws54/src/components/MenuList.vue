<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <MenuListItem
    v-for="(me,index) in menuList" :key ="index"
    :me="me"
    />
    
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  
  methods: {
    // selectMenu: function () {
    //   this.$store.stage.menuList
    // },
  },
  computed : {
    menuList() {
      return this.$store.state.menuList
    },
  }
}
</script>

<style>

</style>