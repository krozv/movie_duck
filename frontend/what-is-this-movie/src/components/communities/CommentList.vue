<template>
    <div>
        <div class="comments-each">
            <h4>총 {{ comments.length }}개</h4>
            <hr>
        </div>
        <div v-for="comment in comments" :key="comment.id" class="comment">
            <div class="comments">
              <span>{{ comment.content }}</span>
              <div class="btn">
                <button @click="editComment(comment)">Edit</button>
                <button @click="deleteComment(comment.id)">Delete</button>
                <button @click="toggleReplies(comment.id)">대댓글</button> <!-- 대댓글 버튼 추가 -->
              </div>
            </div>
            <hr>
            <div v-if="showReplies[comment.id]" class="commentofcomment">
                <CommentOfComment 
                :movie-id="movieId"
                :comment-id="comment.id"
                />
                <hr>
            </div>
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
import { ref, reactive, onMounted } from 'vue'
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
const showReplies = reactive({})

const fetchComments = () => {
    axios.get(
        `${store.API_URL}/api/movie/${props.movieId}/comments/`)
        .then(response => {
            comments.value = response.data
            response.data.forEach(comment => {
                showReplies[comment.id] = false // 각 댓글에 대한 초기 상태 설정
            })
        })
        .catch(error => {
            console.error('Failed to fetch comments:', error)
        })
}

const toggleReplies = (commentId) => {
    showReplies[commentId] = !showReplies[commentId] // 댓글 상태 토글
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
    display: block;
    margin-left: 50px;
    width: 1050px;
}

.comments {
    display: flex;
    justify-content: space-between;
}

button {
    margin-right: 10px;
}

.comments-each {
    width: 1050px;
    margin-top: 10px;
    margin-left: 50px
}

</style>