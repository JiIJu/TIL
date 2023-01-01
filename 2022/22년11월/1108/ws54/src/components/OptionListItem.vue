<template>
  <div style="padding:10%;background-color:slategrey;border: 1px solid;">
      <span class="text" style="float:left;">
        {{option.type}}
      </span>
      <span>  
      <button
        @click="increase"
        >+</button>
        {{option.count}}
      <button
      @click="decrease"
      >-</button>
      </span>
      <span style="float:right;">{{option.price}}</span>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch('increase',this.option)

    },
    decrease() {
      this.$store.dispatch('decrease',this.option)
    },
  },
}
</script>

<style>
</style>