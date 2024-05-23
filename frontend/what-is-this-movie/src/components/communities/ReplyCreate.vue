<template>
  <v-dialog v-model="warning" width="auto">
    <v-card
      max-width="400"
      :prepend-icon="mdiAlert"
      text="댓글을 작성해주세요"
      title="warning"
    >
      <template v-slot:actions>
        <v-btn class="ms-auto" text="Ok" @click="warning = false"></v-btn>
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
    <v-row class="justify-space-between">
      <div style="width: 80%">
        <v-text-field 
        @keyup.enter="createReply"
        v-model="content"
        class="mx-2"
        label="대댓글을 작성해주세요."
        rows="2"
        hide-details="false"
        ></v-text-field>
      </div>
      <v-spacer></v-spacer>
      <div class="d-flex flex-row">
        <div class="text-caption"><span>{{ content ? content.length : 0 }} / 300</span>  &nbsp;</div>
        <svg-icon v-tooltip:bottom="'Done'" @click="createReply" type="mdi"
          :path="mdiCheck" class="mx-1"></svg-icon>
      </div>
</v-row>
</v-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore';
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiCheck, mdiAlert, mdiComment  } from '@mdi/js'

const props = defineProps({
  moviePk: String,
  commentPk: Number,
})

const store = useCounterStore()
const content = ref('')
const warning = ref(false)
const emits = defineEmits(['fetch-replies'])

const createReply = () => {
  if ( content.value ) {  
  axios({
    method: 'post',
    url: `${store.API_URL}/api/movie/${props.moviePk}/comment/${props.commentPk}/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      content.value = ''; // 폼 초기화
      emits('fetch-replies')
    })
    .catch((error) => {
      console.log(error)
    })
  } else {
    warning.value = true
  }
}

const editWarning = computed(() => {
  return content.value.length > 300 ? true : false
})

const sliceWord = function() {
  content.value = content.value.slice(0, 300)
}
</script>

<style scoped>

</style>