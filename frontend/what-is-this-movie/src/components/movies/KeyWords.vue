<template>
    <div v-if="keywordsNoun && keywordsVerb && keywordsAdj">
      <p>명사 키워드: {{ keywordsNoun.join(', ') }}</p>
      <p>동사 키워드: {{ keywordsVerb.join(', ') }}</p>
      <p>형용사 키워드: {{ keywordsAdj.join(', ') }}</p>
    </div>
    <p v-else>Loading...</p>
</template>

<script setup>
import axios from 'axios'
import { useCounterStore } from '@/stores/userStore'
import { ref, onMounted } from 'vue'

const store = useCounterStore()

const props = defineProps({
    moviePk: String,
})

const keywordsNoun = ref(null)
const keywordsVerb = ref(null)
const keywordsAdj = ref(null)

const fetchKeywords = () => {
    axios.get(
        `${store.API_URL}/api/movie/${props.moviePk}/keywords/`)
        .then(response => {
            keywordsNoun.value = response.data['top_noun']
            keywordsVerb.value = response.data['top_verb']
            keywordsAdj.value = response.data['top_adj']
        })
        .catch(error => {
            console.error('Failed to fetch comments:', error)
        })
    }
    
onMounted(() => {
    fetchKeywords()
})
</script>

<style scoped>
p {
    margin: 0; /* 마진을 완전히 제거 */
    padding: 0; /* 패딩을 완전히 제거 */
}

/* p 태그 사이의 거리를 원하는 만큼 조정할 수 있습니다. 예를 들어: */
p + p {
    margin-top: 2px; /* p 태그 사이에 5px의 간격 추가 */
}
</style>