<template>
    <!-- 단일 영화 컴포넌트 -->
    <div @click="storeMovie" :class="{ 'border-primary': clickCard }" class="card text-bg-dark" style="width: 100%; height: 100%;">
        <img class="card-img" :src="'https://image.tmdb.org/t/p/w300'+moviePosterPath" alt="Card image cap">
        <div class="card-img-overlay">
            <h3 class="card-title" :class="{ 'text-primary': clickCard }">{{ movieTitle }}</h3>
        </div>
    </div>
</template>

<script setup>
import 'bootstrap'
import { ref } from 'vue';

const props = defineProps({
    movieId: Number,
    movieTitle: String,
    moviePosterPath: String,
})

const emits = defineEmits([
    'clickEvent',
])

const clickCard = ref(false)

const storeMovie = function() {
    emits('clickEvent', props.movieId)
    clickCard.value = !clickCard.value
}
</script>

<style scoped>

</style>