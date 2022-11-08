<template>
  <div>
    <button
    @click="pickSize"
    :class="{'is-completed' : size.selected}"
    style="width:100%;height:100%;padding: 9.6%;"
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