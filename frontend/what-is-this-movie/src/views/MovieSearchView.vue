<template>
  <Search 
    @search-emit="callback"
  />
  <h2 class="pa-4 mx-14 my-0">검색 결과</h2>
  <div class="pa-4 mx-14">
    <p v-if="!searchedMovie">검색어 : {{ movie }}</p>
    <p v-else>검색어 : {{ searchedMovie }}</p>
    
    <v-container v-if="searchedItems">
      <v-data-iterator :items="searchedItems">
        <template v-slot:default="{ items }">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            class="mx-auto"
          >
          <v-card 
          class="ma-4" hover
          @click="movieDetailPage(item.raw.id)"
          >
            <v-row>
              <v-col cols="3" class="d-flex align-items-center justify-center">
                <img :src="'https://image.tmdb.org/t/p/w300' + item.raw.poster_path" alt="poster-img" class="movie-image">
              </v-col>
              <v-col >
                <p>제목 : {{ item.raw.title }}</p>
                <p>내용 : {{ item.raw.overview }}</p>
              </v-col>
            </v-row>
          </v-card>
          </v-list-item>
        </template>
      </v-data-iterator>
    </v-container>
    <v-container v-else-if="searchedItems !== undefined">
      <p>검색 결과가 존재하지 않습니다.</p>
    </v-container>
    <v-container v-else>
      <p>데이터를 로딩 중입니다...</p>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, onBeforeMount } from 'vue';
import { useMovieStore } from '@/stores/movies';
import { useRoute, useRouter } from 'vue-router';
import Search from '@/components/Search.vue'
const store = useMovieStore();
const route = useRoute();
const movie = ref(null); // route.params.search 값을 사용하여 초기화
const searchQuery = ref(null);
const searchedItems = ref(null);
const searchedMovie = ref('');

const search = function() {
  if (store.allMovies && store.allMovies.length > 0) {
    const query = searchQuery.value.trim()
    if (query) {
    console.log('search 작동')
    searchedItems.value = store.allMovies.filter(item => item.title.toLowerCase().includes(query.toLowerCase()));
    searchedMovie.value = query;
    searchQuery.value = ''; // 검색 후 검색어 초기화
    } else {
      console.log('검색어 없음')
    }
  } else {
    console.log('데이터 없음')
  }
}

onMounted(() => {
  movie.value = route.params.search || ''
  if (movie.value) {
    searchQuery.value = movie.value
    search();
  }
});

watch(movie, () => {
  console.log('watch 작동')
  if (movie.value) {
    searchQuery.value = movie.value
    search();
  }
}, { immediate: true }
)

const router = useRouter()
const movieDetailPage = function (moviePk) {
 router.push(
   { 
     name: 'boxoffice-detail',
     params: { moviePk : moviePk }
   }
 )
}

const callback = function (data) {
  movie.value = data
}

</script>

<style scoped>
.movie-image {
  width: 100px;
  height: auto;
}
</style>
