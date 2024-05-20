<template>
    <div style="height: 100%">
        <img 
            :src="'https://image.tmdb.org/t/p/w300' + posterPath" alt="poster-img" 
            class="movie-image"
            style="height: 100%"
            >
    </div>
</template>

<script setup>
const props = defineProps({
    posterPath: String,
})
</script>

<style scoped>

</style>