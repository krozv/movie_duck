<template>
    <div v-if="sentiments">
        {{ sentiments }}
    </div>
    <div v-else>
        작성된 댓글이 없어서 예측을 할 수 없습니다.
    </div>
</template>

<script setup>
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore'
import { ref, onMounted, watch } from 'vue'

const store = useCounterStore()
const props = defineProps({
    moviePk: String,
})

onMounted(() => {
    fetchSentiments()
})

const sentiments = ref(null)

const fetchSentiments = () => {
  axios.get(
    `${store.API_URL}/api/movie/${props.moviePk}/sentiments/`)
    .then(response => {
      sentiments.value = response.data
    })
    .catch(error => {
      console.error('Failed to fetch sentiments:', error)
    })
}

</script>

<style scoped>

</style>