<template>
    <div>
        <div class="comments-each">
            <h4>총 {{ comments.length }}개</h4>
            <hr>
        </div>
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <div>
            </div>
                <p>{{ comment.content }}</p>
                <button @click="editComment(comment)">Edit</button>
                <button @click="deleteComment(comment.id)">&ensp;Delete</button>
                <hr>
                <CommentOfComment 
                :movie-id="movieId"
                :comment-id="comment.id"
                />
            <div>
          </div>
          <hr>
        </div>
        <div>
            <CommentCreate 
            :movie-id="movieId"
            :fetch-comments="fetchComments"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import axios from 'axios'
import CommentOfComment from '@/components/communities/CommentOfComment.vue'
import CommentCreate from '@/components/communities/CommentCreate.vue'

const props = defineProps({
    movieId: String,
})

const store = useCounterStore()
const token = store.token
const comments = ref([])

const fetchComments = () => {
    axios.get(
        `${store.API_URL}/api/movie/${props.movieId}/comments/`)
        .then(response => {
            comments.value = response.data
        })
        .catch(error => {
            console.error('Failed to fetch comments:', error)
        })
}

const editComment = (comment) => {
    const updatedContent = prompt('수정 내용:', comment.content)
    if (updatedContent !== null) {
        axios.put(
        `${store.API_URL}/api/movie/${props.movieId}/comment/${comment.id}/`,
        { content: updatedContent },
        { headers: { Authorization: `Token ${token}`}})
            .then(response => {
                fetchComments()  // 댓글 수정 후 목록 갱신
            })
            .catch(error => {
                console.error('Failed to edit comment:', error)
            })
    }
}

const deleteComment = (commentId) => {
    if (confirm('정말 댓글을 삭제하시겠습니까?')) {
        axios.delete(
        `${store.API_URL}/api/movie/${props.movieId}/comment/${commentId}/`,
        { headers: { Authorization: `Token ${token}`}})
            .then(response => {
                fetchComments()  // 댓글 삭제 후 목록 갱신
            })
            .catch(error => {
                console.error('Failed to delete comment:', error)
            })
    }
}


onMounted(() => {
    fetchComments()
    store.fetchUserData()
})
</script>

<style scoped>
.comment {
    margin-left: 50px;
    width: 1050px;
}
.comments-each {
    width: 1050px;
    margin-top: 10px;
    margin-left: 50px
}
</style>