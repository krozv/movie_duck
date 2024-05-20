<template>
    <div>
        <h1>댓글</h1>
        <CommentList :movie-id="movieId"/>
    </div>
</template>

<script setup>
import CommentList from '@/components/communities/CommentList.vue'

defineProps({
    movieId: String
})

</script>

<style scoped>
h1 {
    margin-left: 50px;
}
</style>