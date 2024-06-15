<template >
    <div v-if="videoKey" >
        <YoutubeTrailer :video-key="videoKey"/>
    
    </div>
    <div v-else>
        <p>공식 트레일러 영상이 없습니다.</p>
    </div>
</template>

<script setup>
import  YoutubeTrailer from '@/components/movies/YoutubeTrailer.vue'

const props = defineProps({
    videoKey: String,
})
</script>

<style scoped>

</style>