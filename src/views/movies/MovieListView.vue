<template>
    <div class="movie-slider">
      <button @click="moveLeft">&lt;</button>
        <div class="slider-container">
          <div class="slider" :style="{ transform: 'translateX(' + offsetX + 'px)' }">
            <div v-for="movie in store.movies.results" :key="movie.id" class="movie" @click="movieDetailPage(movie.id)">
              <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">
            </div>
          </div>
        </div>
      <button @click="moveRight">&gt;</button>
    </div>

    <!-- <div class="movie-list">
    <div v-for="movie in store.movies.results" class="movie-card" @click="movieDetailPage(movie.id)">
        <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">

    </div>
</div> -->
<NowPlayingMovies />
  </template>
  
<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from 'vue-router'
import NowPlayingMovies from '@/components/movies/NowPlaying.vue'

const store = useMovieStore()

onMounted(() => {
  store.getMovies()
})

const router = useRouter()
const movieDetailPage = function (movieId) {
    router.push(`/${movieId}`)
}

const slideIndex = ref(0); // 현재 슬라이드 인덱스
const slideWidth = 300; // 각 슬라이드의 너비
const offsetX = ref(0); // 슬라이더 컨테이너의 X 좌표

const moveLeft = () => {
    if (slideIndex.value > 0) {
    slideIndex.value--;
    offsetX.value += slideWidth;
    }
};

const moveRight = () => {
    console.log(store.movies.results)
    if (slideIndex.value < store.movies.results.length - 1) {
    slideIndex.value++;
    offsetX.value -= slideWidth;
    }
};
</script>
<style scoped>
.movie-slider {
  display: flex;
  align-items: center;
}
.slider-container {
  overflow: hidden;
  width: 100%; /* 슬라이더 컨테이너의 너비 조정 */
  margin: 0 10px; /* 왼쪽/오른쪽 버튼과의 간격 */
}
.slider {
  display: flex;
  transition: transform 0.4s ease;
}
.movie {
  flex-shrink: 0;
  width: 300px; /* 각 슬라이드의 너비 */
  padding: 10px;
  background-color: #f0f0f0;
  margin-right: 10px; /* 슬라이드 간격 */
  border-radius: 5px;
}
button {
  border: none;
  background-color: #007bff;
  color: white;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
}
</style>