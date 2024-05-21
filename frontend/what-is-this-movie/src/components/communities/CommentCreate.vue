<template>

  <v-dialog v-model="warning" width="auto">
    <v-card
      max-width="400"
      :prepend-icon="mdiAlert"
      text="댓글을 작성해주세요."
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

  <v-card elevation="0" class="px-1 pt-2" color="">
      <v-form v-if="test" 
      @keyup.enter.prevent = "createComment" 
      @submit.prevent="createComment">
        <v-textarea
          v-model="content"
          class="mx-2"
          label="댓글을 작성해주세요."
          :prepend-icon="mdiComment"
          rows="2"
          clearable
          hide-details="false"
        ></v-textarea>
      
      <v-card-actions class="p-0">
        <v-spacer></v-spacer>
        {{ content.length }} / 300
        <v-btn 
          type="submit" outlined small> 
          <svg-icon type="mdi" :path="mdiCheck "
            color=black
            class="mr-1" 
          ></svg-icon>
        </v-btn>
      </v-card-actions>
      </v-form>
    </v-card>
  </template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore';
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiCheck, mdiAlert, mdiComment  } from '@mdi/js'

const props = defineProps({
    moviePk: String,
    fetchComments: Function,
})

const store = useCounterStore()
const content = ref('')
const moviePk = ref(props.moviePk)
const warning = ref(false)
const createComment = () => {
  // console.log(content)
  if ( content.value ) {  
  axios({
    method: 'post',
    url: `${store.API_URL}/api/movie/${moviePk.value}/comment/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      content.value = ''; // 폼 초기화
      props.fetchComments()
    })
    .catch((error) => {
      console.log(error)
    })
  } else {
    warning.value = true
  }
}

const test = true

const editWarning = computed(() => {
  return content.value.length > 300 ? true : false
})

const sliceWord = function() {
  content.value = content.value.slice(0, 300)
}
</script>

<style scoped>
#content {
    border: 1px solid gray;
    resize: none;
}

.comment-card {
    display: flex;
    border: 1px solid gray;
}
.submit {
    position: absolute;
}
</style>