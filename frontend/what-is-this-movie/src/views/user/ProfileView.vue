<template>
    <div>
        <h1>User Profile Page Will Here.</h1>
    </div>
    <h1 v-if="store.userData">안녕하세요, {{ store.userData.username }}님.</h1>
    
</template>

<script setup>
import { useCounterStore } from '@/stores/userStore';
import { onMounted } from 'vue'

const store = useCounterStore()

onMounted(() => {
    console.log(store.userData)
    if (!store.userData) {
        store.fetchUserData()
    }
})
</script>

<style scoped>

</style>
