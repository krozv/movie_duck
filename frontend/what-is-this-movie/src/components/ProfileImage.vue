<template>
  <div >
    test
    <v-img
    width="100"
    aspect-ratio="1/1"
    cover
    
    ></v-img>
  </div>
  <v-btn @click="requestImg">test</v-btn>
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore';
import axios from 'axios'

const store = useCounterStore()
const API_URL = store.API_URL

const props = defineProps({
  imagePath: String,
})

const requestImg = function() {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/static/duck.jpg',
    responseType: 'arraybuffer'
  })
  .then(response => {
    console.log(response)
    const imageData = Buffer.from(response.data, 'binary').toString('base64');
    const imageUrlData = `data:${response.headers['content-type']};base64,${imageData}`;
    // 이미지 데이터를 imageUrlData 변수에 저장하여 사용할 수 있음
    console.log(imageUrlData);
  })
  .catch(error => {
    console.error('Error fetching image:', error);
  })
}
</script>

<style scoped>

</style>