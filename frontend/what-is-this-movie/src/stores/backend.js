import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// 나중에 쓸 일 있으면 아래 수정할 것임
export const useBackendStore = defineStore('backend', () => {
  const userLikeMovies = ref([])
  return { userLikeMovies }
}, { persist: true,})
