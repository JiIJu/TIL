<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickRandom">Pick Lunch</button>
    <p>{{selectedLunch}}</p>
  </div>
</template>

<script>
import _ from 'lodash';

export default {
  name : 'LunchView',
  data() {
    return {
      selectedLunch : lunch()
    }
  },
  methods : {
    pickRandom() {
      this.selectedLunch = _.sample(this.lunch)
    }
  },
  computed: {
    lunch() {
      return this.$routes.params.menu;
    }
  },
}
</script>

<style>

</style>