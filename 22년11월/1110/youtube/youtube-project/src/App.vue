<template>
  <div id="app">
    <TheSearchBar/>
    <VideoDetail/>
    <VideoList/>
  </div>
</template>

<script>
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'
import TheSearchBar from '@/components/TheSearchBar'
export default {
  name: 'App',
  data() {
    return {
      videoList: []
    }
  },
  components: {
    VideoDetail,
    VideoList,
    TheSearchBar,
  }
}
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
