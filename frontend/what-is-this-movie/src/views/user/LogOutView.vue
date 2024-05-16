<template>
    <div>

    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

// const alertMessage = () => {

// }

// const logout = () => {
//   userStore.logout()
// }

onMounted(() => {

})
</script>

<style scoped>

</style>