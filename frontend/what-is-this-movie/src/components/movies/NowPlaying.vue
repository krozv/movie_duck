<template>
    <h2>현재 상영중인 영화</h2>
    <div class="movie-slider">
      <button @click="moveLeft">&lt;</button>
        <div class="slider-container">
          <div class="slider" :style="{ transform: 'translateX(' + offsetX + 'px)' }">
            <div v-for="movie in nowPlayingMovies" :key="movie.id" class="movie" @click="movieDetailPage(movie.id)">
              <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">
            </div>
          </div>
        </div>
      <button @click="moveRight">&gt;</button>
    </div>

    <!-- <div>
        <p v-for="movie in nowPlayingMovies">
            <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">
            <p>제목 : {{ movie.title }}</p>
            <p>별점 : {{ movie.vote_average }}</p>
        </p>
    </div> -->

</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from 'vue-router'

const nowPlayingMovies = ref([])
const apiKey = '6b9a23f96ce34df2a77e6d0e76769d05'

const getMovies = function() {
    axios({
      method: 'get',
      params: {page: '1'},
      url: "https://api.themoviedb.org/3/movie/now_playing?api_key=" + apiKey + "&language=ko-KR&page=1",
      }
    )
    .then((response) => {
      nowPlayingMovies.value = response.data.results
    })
    .catch((error) => {
      console.log(error)
    })
  }

const store = useMovieStore()
const router = useRouter()
const movieDetailPage = function (movieId) {
    router.push({ 
      name: 'movie-detail',
      params: { movieId : movieId }
    })
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
    if (slideIndex.value < nowPlayingMovies.value.length - 1) {
    slideIndex.value++;
    offsetX.value -= slideWidth;
    }
};
onMounted(() => {
    getMovies()
})
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
h2 {
    margin-left: 50px;
}
</style>