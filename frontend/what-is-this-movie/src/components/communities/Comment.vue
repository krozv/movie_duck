<template>
    <div>
        <h1>댓글</h1>
        <CommentCreate :movie-id="movieId"/>
        <CommentList />
    </div>
</template>

<script setup>
import CommentList from '@/components/communities/CommentList.vue'
import CommentCreate from '@/components/communities/CommentCreate.vue'

defineProps({
    movieId: String
})

</script>

<style scoped>

</style>