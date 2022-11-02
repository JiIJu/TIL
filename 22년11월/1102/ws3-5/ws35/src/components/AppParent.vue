<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input = "fromParent">
    <h3>App : {{appData}}</h3>
    <h3>Parent : {{parentData}}</h3>
    <h3>Child : {{childData}}</h3>
    <AppChild :app-data="appData" :parent-data="parentData" @from-child="fromChild"/>
</div>
</template>

<script>
import AppChild from './AppChild.vue';
export default {
  name : "AppParent",
  components : {AppChild},
  props : {
    appData : String,
  },
  data() {
    return {
      partentData:'',
      childData : '',
    }
  },
  methods : {
    fromParent() {
      this.$emit('from-parent',this.parentData)
    },
    fromChild(child) {
      this.childData = child
      this.$emit('from-child',this.childData)
    }
  }
}
</script>

<style>

</style>