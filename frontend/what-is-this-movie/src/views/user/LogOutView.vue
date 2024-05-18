<template>
    <div>

    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'

const userStore = useCounterStore()
const router = useRouter()

// const alertMessage = () => {

// }

const logout = () => {
  userStore.logout()
}

onMounted(() => {
    logout()
})
</script>

<style scoped>

</style>