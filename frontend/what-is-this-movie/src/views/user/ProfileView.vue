<template>
    <div>
        <h1>User Profile Page Will Here.</h1>
    </div>
    <h1 v-if="userStore.userData">안녕하세요, {{ userStore.userData.username }}님.</h1>
    <hr>
    <h3>좋아요한 영화 목록</h3>
    <div class="row">
            <div class="col-md-2 mt-1" v-for="movie in likeMovies" :key = movie.id>
                <MovieComponent
                :movie-id="movie.movie_id"
                :movie-title="movie.title"
                :movie-poster-path="movie.poster_path"/>
            </div>
        </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore';
import { useBackendStore } from '@/stores/backend';
import axios from 'axios';
import { onMounted, ref } from 'vue'
import MovieComponent from '@/components/recommend/MovieComponent.vue';

const userStore = useCounterStore()
const store = useBackendStore()
const likeMovies = ref(null)

onMounted(() => {
    console.log(userStore.userData)
    if (!userStore.userData) {
        userStore.fetchUserData()
    }
})

const userLikeMovies = function () {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/recommend/likemovie/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        },
    })
    .then((res) => {
        console.log(res)
        likeMovies.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
}

userLikeMovies()

</script>

<style scoped>

</style>
