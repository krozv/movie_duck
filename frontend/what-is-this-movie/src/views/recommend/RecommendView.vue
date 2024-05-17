<template>
    <div class="container">
        <h1>영화 선택 창</h1>
        <p>영화를 10개 이상 골라주세요.</p>
        <p>{{ count }}개를 골랐습니다.</p>
        <div class="row">
            <div class="col-md-3 mt-1" v-for="movie in movies" :key = movie.id>
                <MovieComponent
                @click-event="storeMovie"
                :movie-id="movie.movie_id"
                :movie-title="movie.title"
                :movie-poster-path="movie.poster_path"/>
            </div>
        </div>
        <button class="btn btn-primary">다른 영화</button>
        <button class="btn btn-primary" @click="sendMovies">선택 완료</button>
    </div>
</template>
  
<script setup>
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'
import axios from 'axios'
import MovieComponent from '@/components/recommend/MovieComponent.vue';

const userStore = useCounterStore()
const router = useRouter()
const movies = ref([])
const userLikeMovies = ref([])
const count = ref(0)

watch(userLikeMovies, () => {
    if (userLikeMovies.value){
        count.value = userLikeMovies.value.length
        if (userLikeMovies.value.length >= 10) {
            console.log('영화 10개를 채웠습니다.')
            // 보내기 버튼 활성화
        }
    }
    }, { deep: true }
)

onMounted(() => {
axios({
    method: 'get',
    url: `${userStore.API_URL}/api/recommend/`,
})
    .then((res) => {
        movies.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
// localStorage에 저장한 사용자가 선택한 movieId를 저장함. 페이지를 새로고침(렌더링)할 때마다 작동
userLikeMovies.value = JSON.parse(localStorage.getItem('likedMovies'))
})

const storeMovie = function(movieId) {
    console.log(movieId)
    let isAlreadyLiked
    if (userLikeMovies.value){
        isAlreadyLiked = userLikeMovies.value.some(Id => Id === movieId)
    } else {
        isAlreadyLiked = false
    }
    if (!isAlreadyLiked) {
        if (userLikeMovies.value){
            userLikeMovies.value.push(movieId)
        } else {
            userLikeMovies.value = [movieId]
        }
    } else {
        userLikeMovies.value.pop(movieId)
    }
    console.log(userLikeMovies.value)
    localStorage.setItem('likedMovies', JSON.stringify(userLikeMovies.value))
}

const sendMovies = function () {
    console.log(userLikeMovies.value)
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/recommend/`,
        data: {
            userLikeMovies: userLikeMovies.value,
        }
    })
        .then((res) => {
            console.log(res)
            router.push({ 'name': 'recommend-result' })
        })
        .catch((err) => {
            console.log(err)
        })
}

  </script>
  
  <style scoped>

  </style>