<template>
  <h2 class="pt-4 px-4 mx-14 my-0">아직 안 나온 영화</h2>
  <v-slide-group
      class="px-2"
      selected-class="bg-success"
      show-arrows
    >
      <v-slide-group-item
        v-for="popularMovie in store.popularMovies" 
        :key="popularMovie.id"
        v-slot="{ selectedClass }"
      >
        <v-card
          :class="['ma-4', selectedClass]"
          @click="movieDetailPage(popularMovie.id)"
          hover
        >
        <Poster 
          :poster-path="popularMovie.poster_path"
        />
          
        </v-card>
      </v-slide-group-item>
    </v-slide-group>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from 'vue-router'
import Poster from '@/components/movies/Poster.vue'

const store = useMovieStore()

onMounted(() => {
   // boxoffice 순위 불러옴
  store.popular()
   
})
const router = useRouter()
const movieDetailPage = function (moviePk) {
 router.push(
   { 
     name: 'boxoffice-detail',
     params: { moviePk : moviePk }
   }
 )
}
</script>

<style scoped>

</style>