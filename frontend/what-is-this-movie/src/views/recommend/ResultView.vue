<template>
    <div>
        <h1>결과 목록</h1>
        {{ store.userLikeMovies }}
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore'
import { useBackendStore } from '@/stores/backend';
import { onMounted } from 'vue';
import axios from 'axios'

const store = useBackendStore()
const userStore = useCounterStore()

onMounted(() => {
    // console.log(store.userLikeMovies)
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/recommend/`,
        data: {
            userLikeMovies: store.userLikeMovies,
        }
    })
        .then((res) => {
            console.log(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
})
</script>

<style scoped>

</style>