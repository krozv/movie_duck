<template>
  <div v-if="movie.id" class="container">
      <transition>
          <img 
          :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" 
          alt="poster-img" 
          class="movie-image"
          >
      </transition>
      <div class="movie-info">
        <p>제목 : {{ movie.title }}</p>
        <p>개봉일 : {{ movie.release_date }}</p>
        <p>러닝타임 : {{ movie.runtime }}</p>
        <p>평점 : {{ score }}점</p>
        <p>
          장르 : 
          <span v-for="genre in movie.genres">
              {{ genre.name }},  
          </span>
        </p>
        <p>내용 : {{ movie.overview }}</p>
        <div v-if="keywords">
          <p>명사 키워드 : <span>{{ keywords.top_noun }}</span></p>
          <p>동사 키워드 : <span>{{ keywords.top_verb }}</span></p>
          <p>형용사 키워드 : <span>{{ keywords.top_adj }}</span></p>
        </div>
        <p v-else>로딩중 입니다 ~~</p>
      </div>
  </div>
  
  <p v-else>로딩중 !!!</p>
  
  <!-- <div v-if="videoId"> -->
  <div class="trailer">
    <p style="font-size: 30px; margin-left: 100px;">트레일러</p>
    <button @click="modalOpen()">
      <img :src="thumbnailUrl" alt="YouTube Thumbnail" class="thumbnail"/>
    </button>
    <div class="modal-wrap" v-show="modalCheck">
      <div class="modal-container">
          <iframe
          :width="1024"
          :height="600"
          :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen/>
        <div class="modal-btn">
          <button @click="modalOpen">닫기</button>
          <button @click="modalOpen">확인</button>
        </div>
      </div>
    </div>
  </div>
  <div>
      <Comment :movie-id="movieId"/>
  </div>
  </template>
    
  <script setup>
  import { useRoute } from 'vue-router'
  import { ref, onMounted, computed } from 'vue'
  import { useCounterStore } from '@/stores/userStore'
  import Comment from '@/components/communities/Comment.vue'
  import axios from 'axios'

  const store = useCounterStore()
  const route = useRoute()
  const movieId = route.params.movieId
  
  const apiKey = import.meta.env.VITE_TMDB_API_KEY
  const movie = ref({})
  const score = ref(null)
  
  const videoId = ref('')
  onMounted(() => {
      fetchKeywords()
  })
  axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movieId}?api_key=` + apiKey + "&language=ko-KR",
        }
      )
      .then((response) => {
          console.log()
          movie.value = response.data
          const title = response.data.title
          score.value = movie.value.vote_average.toFixed(1)
          movieRequest(title)
      })
      .catch((error) => {
        console.log(error)
      })
  
  const youtube = ref({})
  const youtubeApiKey = "AIzaSyCpTe_PihmSAxCNKyY0r55h6cRF4NcDALA"; // 유효한 YouTube Data API 키를 입력합니다.
  const apiUrl = `https://www.googleapis.com/youtube/v3/search`; // API URL
  const thumbnailUrl = ref('')
  
  
  const movieRequest = function(title) {
      const url = `${apiUrl}?key=${youtubeApiKey}&q=${title}+트레일러&part=snippet&type=video`;
      axios({
          method: 'get',
          url: url,
      })
      .then((response) => {
          youtube.value = response.data
          videoId.value = youtube.value.items[0].id.videoId
          thumbnailUrl.value = youtube.value.items[0].snippet.thumbnails.default.url
      })
      .catch((error) => {
          console.log(error)
  })
  }
  
  const modalCheck = ref(false)
  function modalOpen() {
      modalCheck.value = !modalCheck.value
  }

  
  const keywords = ref(null)

  const fetchKeywords = () => {
    axios.get(
        `${store.API_URL}/api/movie/${movieId}/keywords/`)
        .then(response => {
          keywords.value = response.data
        })
        .catch(error => {
            console.error('Failed to fetch comments:', error)
        })
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
  
  img {
      width: 300px;
      height: 429px;
  }
  .container {
      display: flex;
      margin-top: 50px;
      margin-left: 50px;
      margin-bottom: 50px;
  }
  
  .movie-info {
      margin-left: 50px;
      margin-top: 50px;
      text-align: center;
      width: 930px;
  }
  
  .movie-info p {
      margin-top: 10px;
  }
  
  .thumbnail {
      margin-left: 25%;
      width: 240px;
      height: 180px;
  }
  
  .trailer {
    margin-bottom: 60px;
  }
  </style>
  