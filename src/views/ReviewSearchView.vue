<template>
    <h1>ReviewSearchView</h1>
    <div>
    <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요">
    <button @click="search">검색</button>
    <ul v-if="searchedItems.length > 0">
      <li v-for="item in searchedItems" :key="item.id">
        <img :src="'https://image.tmdb.org/t/p/w300' + item.poster_path" alt="poster-img" class="movie-image">
        <p>제목 : {{ item.title }}</p>
        <p>내용 : {{ item.overview }}</p>
      </li>
    </ul>
    <p v-else>검색 결과가 없습니다.</p>
  </div>
</template>
  
<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movies'

const store = useMovieStore()

onMounted(() => {  
  store.getMovies()
})

const items = store.movies.results
const searchQuery = ref('');
const searchedItems = ref([]);

console.log(items)
function search() {
    const query = searchQuery.value
    searchedItems.value = items.filter(item => item.title === query );

}
</script>
  
<style scoped>
  
</style>