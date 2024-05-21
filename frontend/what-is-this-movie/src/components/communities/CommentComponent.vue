<template>
  <v-dialog v-model="deleteAlert" width="auto" @keyup.enter="[deleteAlert = false, deleteComment()]">
    <v-card max-width="400" 
    :prepend-icon="mdiAlert" text="정말 댓글을 삭제하시겠습니까?" 
    
    title="warning">
      <template v-slot:actions >
        <v-btn text="Cancel" @click="[deleteAlert = false]"></v-btn>
        <v-btn class="ms-auto" text="Ok" 
        @click="[deleteAlert = false, deleteComment()]" 
        color="warning"></v-btn>
      </template>
    </v-card>
  </v-dialog>
  
  <v-dialog v-model="editWarning" width="auto">
    <v-card max-width="400" :prepend-icon="mdiAlert" text="300자 넘길 수 없음" title="warning">
      <template v-slot:actions>
        <v-btn class="ms-auto" text="Ok" @click="sliceWord"></v-btn>
      </template>
    </v-card>
  </v-dialog>
  
    <v-container>
      <v-row justify="space-between">
        <div style="display: flex; width: 100%;">
          <div v-if="!editAlert" class="comment-content">
            {{ comment.content }}
          </div>
          <div v-else style="width: 100%;">
            <v-textarea @keyup.enter="[editAlert = !editAlert, editComment()]" v-model="comment.content"
              class="" rows="2" hide-details="true"
              ></v-textarea>
          </div>
        </div>
        <div justify="end" class="ml-auto">
          {{ comment.content.length }} / 300
          <div v-if="!editAlert">
            <svg-icon v-tooltip:bottom="'Reply'" @click="showReplies = !showReplies" type="mdi" :path="mdiCommentMultipleOutline" class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Edit'" v-if="!editAlert" @click="editAlert = !editAlert" type="mdi" :path="mdiCommentEditOutline"
              class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Delete'" v-if="!editAlert" @click="deleteAlert = true" type="mdi" :path="mdiCommentRemoveOutline" class="mx-1"></svg-icon>
          </div>
          <div v-else>
            <svg-icon v-tooltip:bottom="'Done'" @click="[editAlert = !editAlert, editComment()]" type="mdi" :path="mdiCommentCheckOutline"
            class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Reply'" @click="showReplies = !showReplies" type="mdi" :path="mdiCommentMultipleOutline" class="mx-1"></svg-icon>
          </div>
        </div>
      </v-row>
    </v-container>
  <hr>
  {{comment }}
  <div v-if="showReplies" class="commentofcomment">
    <div >
      <ReplyComponent :movie-pk="moviePk" :comment-pk="comment.id"/>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import axios from 'axios'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiAlert, mdiCommentEditOutline, mdiCommentCheckOutline, mdiCommentRemoveOutline, mdiCommentMultipleOutline  } from '@mdi/js'
import ReplyComponent from './ReplyComponent.vue'

const props = defineProps({
  moviePk: String,
  comment: Object,
})

const emits = defineEmits(['deleteEvent'])
const store = useCounterStore()
const token = store.token
const showReplies = ref(false)

const toggleReplies = () => {
    showReplies = !showReplies // 댓글 상태 토글
}

const editAlert = ref(false)

const editWarning = computed(() => {
  return props.comment.content.length > 300 ? true : false
})

const sliceWord = function() {
  props.comment.content = props.comment.content.slice(0, 300)
  editComment()
}

const editComment = () => {
  axios.put(
  `${store.API_URL}/api/movie/${props.moviePk}/comment/${props.comment.id}/`,
  { content: props.comment.content },
  { headers: { Authorization: `Token ${token}`}})
      .then(response => {
      })
      .catch(error => {
          console.error('Failed to edit comment:', error)
      })
}

const deleteAlert = ref(false)
const deleteComment = () => {
    axios.delete(
    `${store.API_URL}/api/movie/${props.moviePk}/comment/${props.comment.id}/`,
    { headers: { Authorization: `Token ${token}`}})
        .then(() => {
          emits('deleteEvent')
        })
        .catch(error => {
          console.error('Failed to delete comment:', error)
        })
}

const replies = ref([])

const fetchReplies = () => {
  axios.get(`${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentId}/`, {
    headers: { Authorization: `Token ${token}` }
  })
    .then(response => {
      console.log(response)
      replies.value = response.data.replies
    })
    .catch(error => {
      console.error('Failed to fetch replies:', error)
    })
}

onMounted(() => {
  fetchReplies()
  store.fetchUserData()
})

</script>

<style scoped>
.comment-content {
  overflow-wrap: break-word; /* 긴 단어가 줄바꿈되도록 함 */
  white-space: normal; /* 공백을 정상적으로 처리하여 줄바꿈을 허용 */
  max-width: 100%; /* 최대 너비를 100%로 설정하여 부모 요소의 너비를 넘어가지 않도록 함 */
}
</style>