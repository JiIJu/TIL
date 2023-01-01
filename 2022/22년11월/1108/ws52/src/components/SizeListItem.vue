<template>
  <div>
    <button
    @click="pickSize"
    :class="{'is-completed' : size.selected}"
    >{{size.name}} {{size.price}}</button>
    
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods : {
    pickSize() {
      this.$store.dispatch('pickSize',this.size)
    },
  }
}
</script>

<style>
.is-completed {
    background-color: aquamarine;
  }
</style>