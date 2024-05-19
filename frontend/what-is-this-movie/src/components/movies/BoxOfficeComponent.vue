<template>
  <h2 class="pa-4">Box Office 순위</h2>
  <v-slide-group
      class="pa-4"
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
        <BoxOfficePoster 
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
</script>

<style scoped>

</style>