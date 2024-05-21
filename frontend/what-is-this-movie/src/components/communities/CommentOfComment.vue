<template>
    <div class="replies">
        <div v-for="reply in replies" :key="reply.id" class="reply">
          <ReplyComponent
          :movie-pk="moviePk" :comment-pk="comment.pk" @delete-event="callback"/>
        </div>
        <hr>
      <form @submit.prevent="createReply">
        <textarea v-model.trim="newReplyContent"></textarea>
        <button type="submit" class="reply-submit">대댓글 작성</button>
      </form>
      <v-form>

      </v-form>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore'
import ReplyComponent from '@/components/communities/ReplyComponent.vue'

const props = defineProps({
  moviePk: String,
  commentId: Number,
})
  
const store = useCounterStore()
const token = store.token
const replies = ref([])
const newReplyContent = ref('')

const editAlert = ref(false)

const editWarning = computed(() => {
  return props.comment.content.length > 300 ? true : false
})

const sliceWord = function() {
  props.comment.content = props.comment.content.slice(0, 300)
  editComment()
}
const createReply = () => {
    axios.post(`${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentId}/`, 
    { content: newReplyContent.value }, 
    { headers: { Authorization: `Token ${token}` }}
    )
    .then(response => {
      fetchReplies()  // 대댓글 작성 후 목록 갱신
      newReplyContent.value = ''  // 폼 초기화
    })
    .catch(error => {
      console.error('Failed to create reply:', error)
    })
  }

const fetchReplies = () => {
  axios.get(`${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentId}/`, {
    headers: { Authorization: `Token ${token}` }
  })
    .then(response => {
      replies.value = response.data.replies
  })
    .catch(error => {
      console.error('Failed to fetch replies:', error)
  })
  }

  const editReply = (reply) => {
    const updatedContent = prompt('수정 내용:', reply.content)
    if (updatedContent !== null) {
      axios.put(`${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentId}/${reply.id}/`, {
        content: updatedContent
      }, {
        headers: { Authorization: `Token ${token}` }
      })
      .then((res) => {
        fetchReplies()  // 대댓글 수정 후 목록 갱신
      })
      .catch(error => {
        console.error('Failed to edit reply:', error)
      })
    }
  }
  
  const deleteReply = (replyId) => {
    if (confirm('정말 대댓글을 삭제하시겠습니까?')) {
      axios.delete(`${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentId}/${replyId}/`, {
        headers: { Authorization: `Token ${token}` }
      })
      .then(response => {
        fetchReplies()  // 대댓글 삭제 후 목록 갱신
      })
      .catch(error => {
        console.error('Failed to delete reply:', error)
      })
    }
  }
  
  
onMounted(() => {
  fetchReplies()
  store.fetchUserData()
})

</script>

<style scoped>
textarea {
    width: 60%;
    height: 34px;
    margin-top: 10px;
    padding: 5px;
    border: 1px solid gray;
    overflow: hidden;
    resize: none;
  }

.replies {
    margin-left: 50px;
    
}
.reply-submit {
  margin-left: 20px;
}

.reply {
  display: flex;
  justify-content: space-between;
}

.btn {
  margin-right: 62px;
}
</style>