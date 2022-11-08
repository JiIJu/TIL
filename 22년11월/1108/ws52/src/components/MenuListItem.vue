<template>
  <div class="container">
    <button
    @click="pickMenu"
    :class="{'is-completed' : me.selected}"
    >
    <img :src="me.image" style="width: 50px; height:50px;">
    {{me.name}} {{me.price}}
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