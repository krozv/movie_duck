<template>
    <div>
        <h1>댓글</h1>
        <CommentCreate />
        <CommentList />
    </div>
</template>

<script setup>
import CommentList from '@/components/communities/CommentList.vue'
import CommentCreate from '@/components/communities/CommentCreate.vue'

</script>

<style scoped>
div {
    margin-top: 20px;
    margin-left: 60px;
}

h1 {
    margin-left: 50px;
}
</style>