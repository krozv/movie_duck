<template>
    <h1>boxoffice detail view</h1>
    <div v-if="moviePk" class="container">
        <div class="row">
            <div class="col-md-6">
                <p>poster 넣을 예정</p>
            </div>
            <div class="col-md-6">
                <h1>{{ store.movie.title }}</h1>
                <p>{{ store.movie.overview }}</p>
            </div>
        </div>
        <hr>
        <div class="row">
            <p>youtube trailer 예정</p>
        </div>
        <hr>
        <div>
            <Comment />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movies';
import Comment from '@/components/communities/Comment.vue'
const route = useRoute()
const moviePk = route.params.moviePk
const store = useMovieStore()
// 수정중!!!!!!!!!!!!!
onMounted(() => {
    store.getMovies(moviePk)
    console.log(store.movie)
})
</script>

<style scoped>

</style>