<template>
    <h4>댓글 ({{ comments ? comments.length : 0 }})</h4>
        <hr>
    <div v-for="comment in comments" :key="comment.id" class="comment">
        <CommentComponent :movie-pk="moviePk" :comment="comment" @delete-event="callback"/>
    </div>
    <div>
        <CommentCreate 
        :movie-pk="moviePk"
        @fetch-comments="callback"
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
const comments = ref(null)

// 댓글 삭제 시 reload
const callback = function() {
    fetchComments()
    store.fetchUserData()
}

const fetchComments = () => {
    console.log('fetch comment')
    axios.get(
        `${store.API_URL}/api/movie/${props.moviePk}/`,
        { headers: { Authorization: `Token ${token}`}})
        .then(response => {
            console.log(response.data.comments)
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