<template>
  <div id="app">
    <VideoComponent />
  </div>
</template>

<script>
import VideoComponent from "./components/VideoComponent.vue";

export default {
  name: "App",
  components: {
    VideoComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
