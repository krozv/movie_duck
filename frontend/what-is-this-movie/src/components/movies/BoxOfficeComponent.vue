<template>
  <h2 class="pa-4 mx-14 my-0">Box Office 순위</h2>
  <v-slide-group
      class="px-2"
      selected-class="bg-success"
      show-arrows
    >
      <v-slide-group-item
        v-for="boxoffice in store.boxOfficeMovies" 
        :key="boxoffice.movie[0].movie_id"
        v-slot="{ selectedClass }"
      >
        <v-card
          :class="['ma-4', selectedClass]"
          @click="movieDetailPage(boxoffice.movie[0].pk)"
          hover
        >
        <Poster 
          :poster-path="boxoffice.movie[0].poster_path"
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
   store.boxOffice()
   
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