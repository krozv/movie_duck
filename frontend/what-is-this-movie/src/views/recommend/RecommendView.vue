<template>
    <div class="px-4 mx-14">
        <h3 class="py-2">영화 선택 창</h3>
        <p>영화를 10개 이상 골라주세요.</p>
        <p>{{ count }}개를 골랐습니다.</p>
        <div class="row">
            <div class="col-6 col-md-3 col-xl-2 mt-1" v-for="movie in movies" :key = movie.id>
                <MovieComponent
                @click-event="storeMovie"
                :movie-id="movie.movie_id"
                :movie-title="movie.title"
                :movie-poster-path="movie.poster_path"/>
            </div>
        </div>
        <div class="d-flex py-4 justify-content-center">
        <button @click="reset" class="btn btn-warning">다른 영화</button>
        <button @click="goResult" v-show="moveToResult" class="btn btn-warning ml-4">선택 완료</button>
        </div>

    </div>
</template>
  
<script setup>
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import { useBackendStore } from '@/stores/backend'
import { useRouter } from 'vue-router'
import axios from 'axios'
import MovieComponent from '@/components/recommend/MovieComponent.vue';

const userStore = useCounterStore()
const movies = ref([])
const store = useBackendStore()
const count = ref(0)
const moveToResult = ref(false) // 영화를 10개 이상 골랐을 때 전송 가능

watch(store, () => {
    console.log('watch 작동')
    if (store.userLikeMovies){
        count.value = store.userLikeMovies.length
        if (store.userLikeMovies.length >= 10) {
            console.log('영화 10개를 채웠습니다.')
            // 보내기 버튼 활성화
            moveToResult.value = true
        } else {
            moveToResult.value = false
        }
    }
    }, { deep: true }
)

onMounted(() => {
axios({
    method: 'get',
    url: `${userStore.API_URL}/api/recommend/`,
    headers: {
            Authorization: `Token ${userStore.token}`
        },
})
    .then((res) => {
        movies.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
// localStorage에 저장한 사용자가 선택한 movieId를 저장함. 페이지를 새로고침(렌더링)할 때마다 작동
store.userLikeMovies = JSON.parse(localStorage.getItem('likedMovies'))
})

const storeMovie = function(movieId) {
    console.log(movieId)
    let isAlreadyLiked = store.userLikeMovies?.includes(movieId)
    if (!isAlreadyLiked) {
        if (store.userLikeMovies){
            store.userLikeMovies.push(movieId)
        } else {
            store.userLikeMovies = [movieId]
        }
    } else {
        store.userLikeMovies.pop(movieId)
    }
    localStorage.setItem('likedMovies', JSON.stringify(store.userLikeMovies))
}
const reset = function () {
    window.location.reload()
}
const router = useRouter()
const goResult = function () {
    router.push({
        name: 'recommend-result'
    })
}
  </script>
  
  <style scoped>

  </style>