<template >
    <div v-if="videoKey" class="col-3">
    <iframe
        width="100%"
        :src="`https://www.youtube.com/embed/${videoKey}`"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    </div>
    <div v-else>
        <p>공식 트레일러 영상이 없습니다.</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
    videoId: String,
    videoSite: String,
    videoKey: String,
})
</script>

<style scoped>

</style>