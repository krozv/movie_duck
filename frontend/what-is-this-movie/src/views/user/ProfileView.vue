<template>
    
    <div class="pa-4">
    <h2 v-if="userStore.userData">안녕하세요, {{ userStore.userData.username }}님.</h2>
    </div>
    <hr>
    <div class="pa-4">
    <h3>좋아요한 영화 목록</h3>
    </div>
    <v-slide-group
        class="pa-4"
        selected-class="bg-success"
        show-arrows
        
    >
        <v-slide-group-item
            v-for="movie in likeMovies" 
            :key = movie.id
            v-slot="{ isSelected }"
            
        >
            <v-card
                :class="['ma-2', isSelected]"
                hover
                height="200"
                weight="100"
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
import { useBackendStore } from '@/stores/backend';
import axios from 'axios';
import { onMounted, ref } from 'vue'
import Poster from '@/components/movies/Poster.vue'

const userStore = useCounterStore()
const store = useBackendStore()
const likeMovies = ref(null)

onMounted(() => {
    console.log(userStore.userData)
    if (!userStore.userData) {
        userStore.fetchUserData()
    }
})

const userLikeMovies = function () {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/recommend/likemovie/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        },
    })
    .then((res) => {
        console.log(res)
        likeMovies.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
}

userLikeMovies()

</script>

<style scoped>

</style>
