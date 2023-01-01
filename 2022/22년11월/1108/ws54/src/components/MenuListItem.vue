<template>
  <div class="container">
    <button
    @click="pickMenu"
    :class="{'is-completed' : me.selected}"
    style="width:100%;height:100%;padding: 7%;"
    >
    <img :src="me.image" style="width: 50px; height:50px; float:left;">
    <span style="text-align:center">{{me.name}}</span> <span style="float:right">{{me.price}}</span>
  </button>
    
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    me: Object,
  },
  computed: {
    // menuList() {
    //   return this.$store.state.menuList
    // },
  },
  methods : {
    pickMenu() {
      this.$store.dispatch('pickMenu',this.me)
    }
  }
}
</script>

<style>
.is-completed {
    background-color: aquamarine;
  }

</style>