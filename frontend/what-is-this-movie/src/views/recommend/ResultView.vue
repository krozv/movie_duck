<template>
<div>
    <h1>추천 결과</h1>
    <ResultComponent
    :search="'genre'"/>
    <ResultComponent
    :search="'actor'"/>
</div>

</template>

<script setup>
import ResultComponent from '@/components/recommend/ResultComponent.vue';


</script>

<style scoped>

</style>