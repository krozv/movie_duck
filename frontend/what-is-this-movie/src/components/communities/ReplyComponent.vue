<template>
  <v-dialog v-model="deleteAlert" width="auto" @keyup.enter="[deleteAlert = false, deleteReply()]">
    <v-card max-width="400" :prepend-icon="mdiAlert" text="🦆정말 삭제할거야?" title="warning">
      <template v-slot:actions>
        <v-btn text="아닝" @click="[deleteAlert = false]"></v-btn>
        <v-btn class="ms-auto" text="삭제" @click="[deleteAlert = false, deleteReply()]" color="warning"></v-btn>
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

  <v-container style="display: flex; width: 100%;">
      <v-row  class="justify-space-between">
        <div v-if="!editAlert" class="text-caption pl-4">
          <span>{{ reply.content }}</span>
        </div>
        <div v-else style="width: 70%;" class="pl-4">
          <v-text-field 
            @keyup.enter="[editAlert = !editAlert, editReply()]" 
            v-model="reply.content" 
            rows="2"
            type="input"
            ></v-text-field>
        </div>
        <v-spacer></v-spacer>
        <div class="d-flex flex-row">
          <div class="text-caption"><span>{{ reply.content.length }} / 300</span>  &nbsp;</div>
          <div v-if="!editAlert">
            <svg-icon v-tooltip:bottom="'Edit'" v-if="!editAlert" @click="editAlert = !editAlert" type="mdi"
              :path="mdiCommentEditOutline" class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Delete'" v-if="!editAlert" @click="deleteAlert = true" type="mdi"
              :path="mdiCommentRemoveOutline" class="mx-1"></svg-icon>
          </div>
          <div v-else>
            <svg-icon v-tooltip:bottom="'Done'" @click="[editAlert = !editAlert, editReply()]" type="mdi"
              :path="mdiCommentCheckOutline" class="mx-1"></svg-icon>
          </div>
      </div>
      </v-row>
  </v-container>
  <hr>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import axios from 'axios'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiCommentEditOutline, mdiCommentCheckOutline, mdiCommentRemoveOutline, mdiAlert  } from '@mdi/js'

const props = defineProps({
  moviePk: String,
  commentPk: Number,
  reply: Object,
})
const store = useCounterStore()
const token = store.token

// 댓글 편집
const editAlert = ref(false)

const editWarning = computed(() => {
  return props.reply.content.length > 300 ? true : false
})

const sliceWord = function() {
  props.reply.content = props.reply.content.slice(0, 300)
  editReply()
}

const editReply = () => {
  axios.put(
  `${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentPk}/${props.reply.id}/`,
  { content: props.reply.content },
  { headers: { Authorization: `Token ${token}`}})
      .then(response => {
      })
      .catch(error => {
          console.error('Failed to edit comment:', error)
      })
}

const emits = defineEmits(['deleteEvent'])
const deleteAlert = ref(false)
const deleteReply = () => {
    axios.delete(
    `${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentPk}/${props.reply.id}/`,
    { headers: { Authorization: `Token ${token}`}})
        .then(() => {
          emits('deleteEvent')
        })
        .catch(error => {
          console.error('Failed to delete comment:', error)
        })
}
</script>

<style scoped>
.v-text-area input {
    font-size: 1.2em;
  }
</style>