<template>
    <div>
        <iframe
        width="100%"
        :src="`https://www.youtube.com/embed/${videoKey}`"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    </div>
</template>

<script setup>
const props = defineProps({
    videoKey: String,
})
</script>

<style scoped>

</style>