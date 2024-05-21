<template>
    <div>
        <h1>댓글</h1>
        <CommentList :movie-pk="moviePk"/>
    </div>
</template>

<script setup>
import CommentList from '@/components/communities/CommentList.vue'

const props = defineProps({
    moviePk: String
})
console.log(props.moviePk)

</script>

<style scoped>
</style>