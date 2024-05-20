<template>
    <hr>
    <div v-if="firstMovies && firstMovies.length > 0">
        <h3><span class="bold-dark">{{ firstMovies[0]['recommend'] }}</span> {{ classification(search)}} 영화를 좋아하시네요</h3>
        <v-slide-group
            class="px-2"
            selected-class="bg-success"
            show-arrows
        >
            <v-slide-group-item
                v-for="movie in firstMovies" 
                :key="movie.id"
                v-slot="{ selectedClass }"
            >
                <v-card
                    :class="['ma-4', selectedClass]"
                    @click="movieDetailPage(movie.pk)"
                    hover
                >
                <Poster 
                    :poster-path="movie.poster_path"
                />
          
                </v-card>
            </v-slide-group-item>
        </v-slide-group>
    </div>
    <hr>
    <div v-if="secondMovies && secondMovies.length > 0">
        <h3><span class="bold-dark">{{ secondMovies[0]['recommend'] }}</span> {{ classification(search)}} 영화를 추천드려요</h3>

        <v-slide-group
            class="px-2"
            selected-class="bg-success"
            show-arrows
        >
            <v-slide-group-item
                v-for="movie in secondMovies" 
                :key="movie.id"
                v-slot="{ selectedClass }"
            >
                <v-card
                    :class="['ma-4', selectedClass]"
                    @click="movieDetailPage(movie.pk)"
                    hover
                >
                <Poster 
                    :poster-path="movie.poster_path"
                />
          
                </v-card>
            </v-slide-group-item>
        </v-slide-group>
    </div>
</template>

<script setup>
import { useBackendStore } from '@/stores/backend';
import { useCounterStore } from '@/stores/userStore'
import { ref } from 'vue';
import axios from 'axios'
import { useRouter } from 'vue-router'
import Poster from '../movies/Poster.vue';
const props = defineProps({
    search: String,
})

const classification = function (search) {
    if (search == 'genre'){
        return '장르'
    } else if ( search == 'actor') {
        return '배우'
    }
}
const store = useBackendStore()
const userStore = useCounterStore()
const firstMovies = ref(null)
const secondMovies = ref(null)
const recommend = function (search) {
    const option = function(search) {
        if (typeof search !== 'string') {
        return '';
    }
    return search.charAt(0).toUpperCase() + search.slice(1);
};
    axios({
        method: 'post',
        url: `${store.API_URL}/api/recommend/${search}/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        },
        data: {
            userLikeMovies: JSON.parse(localStorage.getItem('likedMovies')),
        }
    })
        .then((res) => {
            const firstKey = Object.keys(res.data)[0]
            const secondKey = Object.keys(res.data)[1]
            firstMovies.value = res.data[firstKey]
            secondMovies.value = res.data[secondKey]
            localStorage.setItem(`first${option(search)}Movies`, JSON.stringify(firstMovies.value))
            localStorage.setItem(`second${option(search)}Movies`, JSON.stringify(secondMovies.value))
        })
        .catch((err) => {
            console.log(err)
        })
}
recommend(props.search)

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
.bold-dark {
    font-weight: bold;
    color: rgb(139, 50, 157); /* 어두운 색상 */
}
</style>