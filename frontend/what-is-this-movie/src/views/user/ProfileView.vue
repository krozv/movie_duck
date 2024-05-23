<template>
    <div class="px-4 mx-14">
    <div v-if="userStore.userData" class="pa-4 d-flex">
        <ProfileImage :genre="firstGenre"/>
        <div class="align-self-center">
            <h2 v-if="userStore.userData" class="align-self-center">
                {{ userStore.userData.username }} 
            </h2>
            <p class="m-0">{{ firstGenre }} {{ secondGenre }}</p>
        </div>
    </div>
    <hr>
    <div class="px-4">
    <h3>좋아요한 영화 목록</h3>
    
    </div>
    <div v-if="userStore.userData && userStore.userData.user_liked_movie.length > 0">
        <v-slide-group
            class="px-4 pb-4"
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
    </div>
    <div v-else>
        <p class="px-4 pb-4">🐥: 영화 추천을 받아볼래?
            <v-btn size="small" rounded="xl" @click="moveRecommend">웅><</v-btn>
        </p>
    </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore';
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import Poster from '@/components/movies/Poster.vue'
import ProfileImage from '@/components/ProfileImage.vue'

const userStore = useCounterStore()
const firstGenre = ref(null)
const secondGenre = ref(null)
onMounted(() => {
    if (!userStore.userData) {
        userStore.fetchUserData()
    }
    firstGenre.value = localStorage.getItem('firstGenre')
    secondGenre.value = localStorage.getItem('secondGenre')
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

const moveRecommend = function () {
    router.push(
        {name: 'recommend'}
    )
}
</script>

<style scoped>

</style>
