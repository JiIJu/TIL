<template>
  <div class="vuetube-wrap">
    <div class="container">
      <div class="d-flex justify-content-center">
        <h1 class="mt-3 text-primary">SSAFY TUBE</h1>
      </div>
      <section class="mt-2" v-if="isSelected">
        <div class="ratio ratio-16x9">
          <iframe :src="videoSrc" frameborder="0"></iframe>
        </div>
        <div class="detail m-2">
          <h4>{{ videoTitle }}</h4>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from "axios";

// .env.local 에 키=값 형식으로 저장
// 환경 변수 접근 : process.env.변수이름
// 환경 변수 이름 VUE_APP_ 접두어 필수, 이유? 다른 환경변수 이름과 충돌(중복) 방지
// key 만 숨겨도 됩니다. url은 굳이 감출 필요가 없습니다.
const API_KEY = process.env.VUE_APP_API_KEY;
const API_URL = process.env.VUE_APP_API_URL;
const IFRAME_URL = process.env.VUE_APP_IFRAME_URL;

export default {
  name: "VideoComponent",
  created() {
    axios
      .get(API_URL, {
        params: {
          key: API_KEY,
          type: "video",
          part: "snippet",
          q: "코딩노래",
        },
      })
      .then((res) => {
        let videos = res.data.items;

        this.selectedVideo = videos[0];
        console.log(this.selectedVideo);
      })
      .catch((err) => console.error(err));
  },
  data() {
    return {
      selectedVideo: null,
    };
  },
  computed: {
    videoSrc() {
      return IFRAME_URL + this.selectedVideo.id.videoId;
    },
    videoTitle() {
      return this.selectedVideo.snippet.title;
    },
    isSelected() {
      return this.selectedVideo;
    },
  },
};
</script>

<style></style>
