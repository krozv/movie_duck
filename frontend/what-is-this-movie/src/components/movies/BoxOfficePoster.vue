<template>
    <div class='image-container'>
        <img 
            :src="'https://image.tmdb.org/t/p/w300' + posterPath" alt="poster-img" 
            class="movie-image"
            @mouseover="zoomIn"
            @mouseleave="zoomOut"
            :style="{ transform: zoomStyle, transition: zoomTransition}"
            >
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
const props = defineProps({
    posterPath: String,
})
 // 이미지 커졋다가 작아졋다가
const isZoomed = ref(false)
const zoomIn = () => {
    isZoomed.value = true
}
const zoomOut = () => {
    isZoomed.value = false
}
const zoomStyle = computed(() => {
    return isZoomed.value ? 'scale(1.07)' : 'scale(1)'
})
const zoomTransition = computed(() => {
      return isZoomed.value ? 'transform 0.5s ease' : 'transform 0.5s ease-out'
    })
</script>

<style scoped>
.image-container {
    position: relative;
}

.image-container img {
    position: relative;
    z-index: 1;
    transition: z-index 0.3s;
}

.image-container img:hover {
    z-index: 10;
}
</style>