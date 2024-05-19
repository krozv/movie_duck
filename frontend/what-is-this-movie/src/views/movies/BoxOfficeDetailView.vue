<template>
    <h1>boxoffice detail view</h1>
    <div v-if="store.movie" class="container">
        <div class="row">
            <div class="col-md-6">
                <img 
                :src="'https://image.tmdb.org/t/p/w300' + store.movie.poster_path" 
                alt="poster-img" 
                >
            </div>
            <div class="col-md-6">
                <h1>{{ store.movie.title }}</h1>
                <p>{{ store.movie.overview }}</p>
            </div>
        </div>
        <hr>
            <h4>Youtube Trailer</h4>
            <div class="container">
                <div v-if="store.movie.video && store.movie.video.length > 0">
                    <div class="row">
                    <YoutubeComponent
                        v-for="video in store.movie.video"
                        :video-id="video.video_id"
                        :video-key="video.video_key"
                        :video-site="video.video_site"/>
                    </div>
                </div>
                <div v-else>
                    <p>공식 트레일러 영상이 없습니다.</p>
                </div>
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
import YoutubeComponent from '@/components/movies/YoutubeComponent.vue'
const route = useRoute()
const moviePk = route.params.moviePk
const store = useMovieStore()

onMounted(() => {
    store.getMovies(moviePk)
})

</script>

<style scoped>
</style>