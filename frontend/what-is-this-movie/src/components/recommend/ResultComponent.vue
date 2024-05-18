<template>
    <hr>
    <div v-if="firstMovies && firstMovies.length > 0">
        <h3><span class="bold-dark">{{ firstMovies[0]['recommend'] }}</span> {{ classification(search)}} 영화를 추천드려요</h3>
        <div class="row">
            <div class="col-md-2 mt-1" v-for="movie in firstMovies" :key = movie.id>
                <MovieComponent
                :movie-id="movie.movie_id"
                :movie-title="movie.title"
                :movie-poster-path="movie.poster_path"/>
            </div>
        </div>
    </div>
    <hr>
    <div v-if="secondMovies && secondMovies.length > 0">
        <h3><span class="bold-dark">{{ secondMovies[0]['recommend'] }}</span> {{ classification(search)}} 영화를 추천드려요</h3>
        <div class="row">
            <div class="col-md-2 mt-1" v-for="movie in secondMovies" :key = movie.id>
                <MovieComponent
                :movie-id="movie.movie_id"
                :movie-title="movie.title"
                :movie-poster-path="movie.poster_path"/>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useBackendStore } from '@/stores/backend';
import { ref } from 'vue';
import axios from 'axios'
import MovieComponent from '@/components/recommend/MovieComponent.vue';

const props = defineProps({
    search: String,
})

const classification = function (search) {
    if (search == 'genre'){
        return '장르'
    } else if ( search == 'actor') {
        return '배우'
    }
}
const store = useBackendStore()
const firstMovies = ref(null)
const secondMovies = ref(null)
const recommend = function (search) {
    const option = search => search.charAt(0).toUpperCase() + search.slice(1);
    axios({
        method: 'post',
        url: `${store.API_URL}/api/recommend/${search}/`,
        data: {
            userLikeMovies: JSON.parse(localStorage.getItem('likedMovies')),
        }
    })
        .then((res) => {
            console.log(Object.keys(res.data))
            const firstKey = Object.keys(res.data)[0]
            const secondKey = Object.keys(res.data)[1]
            console.log(firstKey, secondKey)
            firstMovies.value = res.data[firstKey]
            secondMovies.value = res.data[secondKey]
            localStorage.setItem(`first${option}Movies`, JSON.stringify(firstMovies.value))
            localStorage.setItem(`second${option}Movies`, JSON.stringify(secondMovies.value))
        })
        .catch((err) => {
            console.log(err)
        })
}
recommend(props.search)
</script>

<style scoped>
.bold-dark {
    font-weight: bold;
    color: rgb(139, 50, 157); /* 어두운 색상 */
}
</style>