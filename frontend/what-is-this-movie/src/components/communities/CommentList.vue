<template>
    <h1>댓글</h1>
    <div class="comments-each">
        <h4>총 {{ comments.length }}개</h4>
        <hr>
    </div>
    <div v-for="comment in comments" :key="comment.id" class="comment">
        <CommentComponent :movie-pk="moviePk" :comment="comment" @delete-event="callback"/>
    </div>
    <div>
        <CommentCreate 
        :movie-pk="moviePk"
        :fetch-comments="fetchComments"
        />
    </div>

    

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import axios from 'axios'
import CommentCreate from '@/components/communities/CommentCreate.vue'
import CommentComponent from '@/components/communities/CommentComponent.vue'

const props = defineProps({
    moviePk: String,
})

const store = useCounterStore()
const token = store.token
const comments = ref([])

// 댓글 삭제 시 reload
const callback = function() {
    fetchComments()
    store.fetchUserData()
}

const fetchComments = () => {
    axios.get(
        `${store.API_URL}/api/movie/${props.moviePk}/`,
        { headers: { Authorization: `Token ${token}`}})
        .then(response => {
            comments.value = response.data.comments
        })
        .catch(error => {
            console.error('Failed to fetch comments:', error)
        })
}

onMounted(() => {
    fetchComments()
    store.fetchUserData()
})
</script>

<style scoped>
.comment {
    display: block;
}

</style>