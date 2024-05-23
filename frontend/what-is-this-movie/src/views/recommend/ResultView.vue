<template>
<div class="px-4 mx-14">
    <v-row class="d-flex pt-4 justify-content-between">
        <h3 class="m-2">🦆영화를 한 번 추천해봐따🦆</h3>
        <v-btn class="mt-1"
        @click="random">엥? ⭐로</v-btn>
    </v-row>
    <ResultComponent
    v-if="num == 0"
    :search="'genre'"/>
    <ResultComponent
    v-else-if="num == 1"
    :search="'actor'"/>
</div>
</template>

<script setup>
import ResultComponent from '@/components/recommend/ResultComponent.vue';
import { ref } from 'vue'
const num = ref(0)
const random = function () {
    num.value = Math.floor(Math.random() * 2);
}
</script>

<style scoped>

</style>