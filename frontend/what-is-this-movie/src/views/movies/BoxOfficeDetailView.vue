<template>
    <main class="pa-4">
        <div v-if="store.movie" class="container">
        <div class="row">
            <!-- {{ userStore.userData.user_liked_movie }} -->
            <div class="col-md-5">
                <div class="d-flex justify-center">
                    <div>
                    <button 
                    class="heart"
                    :class="{ liked: like }"
                    @click="toggleLike"
                    >
                    {{ like ? '💖' : '🖤' }}
                    </button>
                    <img 
                    :src="'https://image.tmdb.org/t/p/w300' + store.movie.poster_path" 
                    alt="poster-img" 
                    class="pb-2"
                    ></div>
                </div>
            </div>
            <div class="col-md-6">
                <h1>{{ store.movie.title }}</h1>
                <p>{{ store.movie.overview }}</p>
            
            <hr>
                <div>
                    <KeyWords 
                        v-if="store.movie.comments && store.movie.comments.length > 0"
                    :movie-pk="moviePk"/>
                    <div v-else>
                        Loading...
                    </div>
                </div>
                <hr>
                <div>
                    <p>관객들의 영화 평가 :</p>
                    <Sentiments 
                        v-if="store.movie.comments && store.movie.comments.length > 0"
                    :movie-pk="moviePk"/>
                    <div v-else>
                        작성된 댓글이 없어서 예측을 할 수 없습니다.
                    </div>
                </div>
            </div>
        </div>
        <hr>
            <h4>Youtube Trailer</h4>
            <div class="container">
                <div v-if="store.movie.video && store.movie.video.length > 0">
                    <div class="row">
                        <v-slide-group
                        show-arrows>
                            <v-slide-group-item v-for="video in store.movie.video">
                                <YoutubeComponent
                        class="ma-4"
                        :video-key="video.video_key"/>
                            </v-slide-group-item>
                        </v-slide-group>
                    
                    </div>
                </div>
                <div v-else>
                    <p>공식 트레일러 영상이 없습니다.</p>
                </div>
            </div>
        <hr>
        <div>
            <CommentList :movie-pk="moviePk"/>
        </div>
    </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movies';
import CommentList from '@/components/communities/CommentList.vue'
import YoutubeComponent from '@/components/movies/YoutubeComponent.vue'
import Sentiments from '@/components/movies/Sentiments.vue';
import KeyWords from '@/components/movies/KeyWords.vue';
import { useCounterStore } from '@/stores/userStore';
import axios from 'axios';

const route = useRoute()
const moviePk = route.params.moviePk
const store = useMovieStore()
const userStore = useCounterStore()
const like = ref(userStore.getLikeState(moviePk))

onMounted(async() => {
    store.getMovies(moviePk)
    if (!userStore.userData) {
        await userStore.fetchUserData()
    }
})
const toggleLike = () => {
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/recommend/like/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        },
        data: {
            movie_pk: moviePk,
        },
    })
    .then((res) => {
        userStore.toggleLike(moviePk);
        like.value = userStore.getLikeState(moviePk);
        console.log(res)
    })
    .catch((err) => {
        console.log(err)
    })

}

</script>

<style scoped>
.heart {
  position: absolute;
  z-index: 2;
  font-size: 2rem;
  /* font-size: 12em;
  font-family: Copperplate, fantasy;
  line-height: 0.9;
  padding-left: 10px;
  text-shadow: 2px 2px rgb(187, 187, 187); */
}
</style>