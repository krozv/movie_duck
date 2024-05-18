<template>
<div>
    <h1>추천 결과</h1>
    <ResultComponent
    :search="'genre'"/>
    <ResultComponent
    :search="'actor'"/>
</div>

</template>

<script setup>
import { useBackendStore } from '@/stores/backend';
import { ref } from 'vue';
import axios from 'axios'
import ResultComponent from '@/components/recommend/ResultComponent.vue';

const store = useBackendStore()
const firstGenreMovies = ref(null)
const secondGenreMovies = ref(null)
// const recommend = function (search) {
//     const option = search => search.charAt(0).toUpperCase() + search.slice(1);
//     axios({
//         method: 'post',
//         url: `${store.API_URL}/api/recommend/${search}/`,
//         data: {
//             userLikeMovies: JSON.parse(localStorage.getItem('likedMovies')),
//         }
//     })
//         .then((res) => {
//             firstGenreMovies.value = res.data.slice(0, 5)
//             secondGenreMovies.value = res.data.slice(5, 10)
//             localStorage.setItem(`first${option}Movies`, JSON.stringify(firstGenreMovies.value))
//             localStorage.setItem(`second${option}Movies`, JSON.stringify(secondGenreMovies.value))
//         })
//         .catch((err) => {
//             console.log(err)
//         })
// }
// recommend('genre')
// recommend('actor')

</script>

<style scoped>

</style>