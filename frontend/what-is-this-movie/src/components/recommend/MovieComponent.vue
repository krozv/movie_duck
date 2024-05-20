<template>
    <!-- 단일 영화 컴포넌트 -->
    <div @click="storeMovie" :class="{ 'border-warning': clickCard }" class="card text-bg-dark" style="height: 100%;">
        <img class="card-img" 
            :src="'https://image.tmdb.org/t/p/w300'+moviePosterPath" 
            alt="Card image cap"
            style="height: 100%;">
        <div class="card-img-overlay">
            <h4 class="card-title fw-bold  text-dark highlight" 
            :class="{ 'text-warning': clickCard }">{{ movieTitle }}</h4>
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
.highlight {
    background-color: rgba(255,255,255,0.5);
    padding: 3px 5px;
    border-radius: 3px;
}

</style>