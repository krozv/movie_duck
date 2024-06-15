<template>
    <div>
        {{ sentiments }}
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