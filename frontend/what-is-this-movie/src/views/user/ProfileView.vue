<template>
    <div class="pa-4">
       <div v-if="userStore.userData">
        test
        {{ userStore.userData.user_profile }}
        <v-img
        width="100"
        aspect-ratio="1/1"
        cover
        :scr="`${API_URL}+${userStore.userData.user_profile}`"
       ></v-img>
    </div>
    <h2 v-if="userStore.userData">안녕하세요, {{ userStore.userData.username }}님.</h2>
    </div>
    <hr>
    <div class="pa-4">
    <h3>좋아요한 영화 목록</h3>
    </div>
    <v-slide-group
        v-if="userStore.userData"
        class="pa-4"
        selected-class="bg-success"
        show-arrows
        
    >
        <v-slide-group-item
            v-for="movie in userStore.userData.user_liked_movie" 
            :key = movie.id
            v-slot="{ isSelected }"
            
        >
            <v-card
                :class="['ma-2', isSelected]"
                hover
                height="200"
                weight="100"
                @click="movieDetailPage(movie.pk)"
            >
                <Poster
                    :poster-path="movie.poster_path"
                />
                
            </v-card>
        </v-slide-group-item>
    </v-slide-group>
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore';
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import Poster from '@/components/movies/Poster.vue'

const userStore = useCounterStore()
const API_URL = userStore.API_URL
onMounted(() => {
    if (!userStore.userData) {
        userStore.fetchUserData()
    }
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
