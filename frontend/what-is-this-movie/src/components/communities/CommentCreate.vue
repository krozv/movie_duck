<template>
    <div class="comment-card">
      <form @submit.prevent="createComment">
        <div>
          <textarea v-model.trim="content" id="content"></textarea>
          <input type="submit" value="제출" class="submit">
        </div>
      </form>
    </div>
  </template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore';

const props = defineProps({
    movieId: String,
})

const store = useCounterStore()
const content = ref('')
const movieId = ref(props.movieId)  // 예시로 movie_pk를 1로 설정, 실제 값에 맞게 변경하세요.

const createComment = () => {
    axios({
    method: 'post',
    url: `${store.API_URL}/api/movie/${movieId.value}/comment/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log('Comment created:', response.data)
      content.value = ''; // 폼 초기화
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>
#content {
    border: 1px solid gray;
    width: 880px;
    height: 100px;
    margin: 20px;

}

.comment-card {
    display: flex;
    border: 1px solid gray;
    width: 1050px;
    height: 150px;
}
.submit {
    position: absolute;
    width: 100px;
    height: 100px;
    margin-top: 20px;
    border: 1px solid gray;
    
}
</style>