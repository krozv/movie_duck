<template>
    <h1>boxoffice detail view</h1>
    <div v-if="moviePk" class="container">
        <!-- <img 
        :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" 
        alt="poster-img" 
        class="movie-image"
        > -->
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movies';
const route = useRoute()
const moviePk = route.params.moviePk
const store = useMovieStore()
// 수정중!!!!!!!!!!!!!
onMounted(() => {
    store.getMovies()
})
</script>

<style scoped>
.container {
    display: flex;
    margin-top: 50px;
    margin-left: 50px;
    margin-bottom: 50px;
}
</style>