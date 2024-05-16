<template>
    <div>
        <p v-for="movie in nowPlayingMovies">
            <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">
            <p>제목 : {{ movie.title }}</p>
            <p>별점 : {{ movie.vote_average }}</p>
        </p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

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
      // console.log(response.data)
      nowPlayingMovies.value = response.data.results
    })
    .catch((error) => {
      console.log(error)
    })
  }

onMounted(() => {
    getMovies()
})
</script>

<style scoped>

</style>