<template>
  <div class="ml-3">
    <p v-if="!searchedMovie">검색어 : {{ movie }}</p>
    <p v-else>검색어 : {{ searchedMovie }}</p>
  </div>
  <div>
    <input @keyup.enter="search" type="text" v-model="searchQuery" placeholder="검색어를 입력하세요">
    <button @click="search">검색</button>
    <ul v-if="searchedItems.length > 0">
      <li v-for="item in searchedItems" :key="item.id">
        <img :src="'https://image.tmdb.org/t/p/w300' + item.poster_path" alt="poster-img" class="movie-image">
        <p>제목 : {{ item.title }}</p>
        <p>내용 : {{ item.overview }}</p>
      </li>
    </ul>
    <p v-else-if="searchedItems !== undefined">검색 결과가 없습니다.</p>
    <p v-else>데이터를 로딩 중입니다...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useMovieStore } from '@/stores/movies';
import { useRoute } from 'vue-router';

const store = useMovieStore();
const route = useRoute();
const movie = ref(route.params.search || ''); // route.params.search 값을 사용하여 초기화

const searchQuery = ref(movie.value);
const searchedItems = ref([]);
const searchedMovie = ref('');

async function search() {
  if (store.movies.results) {
    const query = searchQuery.value;
    searchedItems.value = store.movies.results.filter(item => item.title.toLowerCase().includes(query.toLowerCase()));
    searchedMovie.value = query;
    searchQuery.value = ''; // 검색 후 검색어 초기화
  }
}

onMounted(async () => {
  await store.getMovies();
  if (movie.value) {
    search();
  }
});
</script>

<style scoped>
.movie-image {
  width: 100px;
  height: auto;
}
</style>
