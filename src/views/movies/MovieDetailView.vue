<template>
<div v-if="movie.id">
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="poster-img" class="movie-image">
    <hr>
    <p>제목 : {{ movie.title }}</p>
    <p>개봉일 : {{ movie.release_date }}</p>
    <p>러닝타임 : {{ movie.runtime }}</p>
    <p>TMDB 평점 : {{ movie.vote_average }}</p>
    <p>장르 : {{ movie.genres[0].name }}</p>
    <hr>
    <p>내용 : {{ movie.overview }}</p>
    <hr>
    <p>공식 예고편 :</p> 
    <button @click="modalOpen()">Modal</button>
    <div v-if="videoId">
        <div class="modal-wrap" v-show="modalCheck">
        <div class="modal-container">
                <iframe
                :width="1024"
                :height="600"
                :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen/>
            <div class="modal-btn">
            <button @click="modalOpen">닫기</button>
            <button @click="modalOpen">확인</button>
            </div>
        </div>
    </div>
</div>
    
    
</div>
<p v-else>로딩중 !!!</p>
</template>
  
<script setup>
import { useRoute } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const route = useRoute()
const movieId = route.params.movieId

const apiKey = '6b9a23f96ce34df2a77e6d0e76769d05'
const movie = ref({})

const videoId = ref('')
axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}?api_key=` + apiKey + "&language=ko-KR",
      }
    )
    .then((response) => {
        console.log()
        movie.value = response.data
        const title = response.data.title
        movieRequest(title)
    })
    .catch((error) => {
      console.log(error)
    })

// const youtube = ref({})
// const youtubeApiKey = "AIzaSyCpTe_PihmSAxCNKyY0r55h6cRF4NcDALA"; // 유효한 YouTube Data API 키를 입력합니다.
// const apiUrl = `https://www.googleapis.com/youtube/v3/search`; // API URL


// const movieRequest = function(title) {
//     const url = `${apiUrl}?key=${youtubeApiKey}&q=${title}+트레일러&part=snippet&type=video`;
//     axios({
//         method: 'get',
//         url: url,
//     })
//     .then((response) => {
//         youtube.value = response.data
//         videoId.value = youtube.value.items[0].id.videoId
//     })
//     .catch((error) => {
//         console.log(error)
// })
// }

const modalCheck = ref(false)
function modalOpen() {
    // const videoId = "Do0slRSdnVM"
    // const test = ref(`https://www.youtube.com/embed/${videoId}?autoplay=1`)
    modalCheck.value = !modalCheck.value
}
</script>

<style scoped>
.modal-wrap {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
}
/* modal or popup */
.modal-container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 550px;
  border-radius: 10px;
  padding: 20px;
  box-sizing: border-box;
}
</style>
