<template>
   <h2>Box Office 순위</h2>
    <div class="movie-slider">
      <button @click="moveLeft">&lt;</button>
        <div class="slider-container">
          <div class="slider" :style="{ transform: 'translateX(' + offsetX + 'px)' }">
            <div v-for="boxoffice in store.boxOfficeMovies" 
              :key="boxoffice.movie[0].movie_id" 
              class="movie" 
              @click="movieDetailPage(boxoffice.movie[0].pk)">
              <BoxOfficePoster 
              :poster-path="boxoffice.movie[0].poster_path"/>
            </div>
          </div>
        </div>
      <button @click="moveRight">&gt;</button>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from 'vue-router'
import BoxOfficePoster from '@/components/movies/BoxOfficePoster.vue'
const store = useMovieStore()

onMounted(() => {
    // boxoffice 순위 불러옴
    store.boxOffice()
    
})
const router = useRouter()
const movieDetailPage = function (moviePk) {
  console.log(moviePk)
  router.push(
    { 
      name: 'boxoffice-detail',
      params: { moviePk : moviePk }
    }
  )
}

const slideIndex = ref(0); // 현재 슬라이드 인덱스
const slideWidth = 300; // 각 슬라이드의 너비
const offsetX = ref(0); // 슬라이더 컨테이너의 X 좌표

const moveLeft = () => {
  if (slideIndex.value > 0) {
  slideIndex.value--;
  offsetX.value += slideWidth;
  }
};

const moveRight = () => {
  if (slideIndex.value < store.boxOfficeMovies.length - 1) {
  slideIndex.value++;
  offsetX.value -= slideWidth;
  }
}

</script>

<style scoped>
.movie-slider {
display: flex;
align-items: center;
margin-bottom: 30px;
}
.slider-container {
overflow: hidden;
width: 100%; /* 슬라이더 컨테이너의 너비 조정 */
margin: 0 10px; /* 왼쪽/오른쪽 버튼과의 간격 */
}
.slider {
display: flex;
transition: transform 0.4s ease;
}
.movie {
flex-shrink: 0;
width: 300px; /* 각 슬라이드의 너비 */
padding: 10px;
margin-right: 10px; /* 슬라이드 간격 */
border-radius: 5px;
}
button {
border: none;
background-color: #007bff;
color: white;
padding: 5px 10px;
border-radius: 3px;
cursor: pointer;
}
h2 {
  margin-left: 50px;
}
</style>