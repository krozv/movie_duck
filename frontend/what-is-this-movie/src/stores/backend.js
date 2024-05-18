import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// 나중에 쓸 일 있으면 아래 수정할 것임
export const useBackendStore = defineStore('backend', () => {
  const userLikeMovies = ref([])
  const genreMovies = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const recommend = function () {
    axios({
        method: 'post',
        url: `${API_URL}/api/recommend/`,
        data: {
            userLikeMovies: store.userLikeMovies,
        }
    })
        .then((res) => {
            genreMovies.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}
  return { userLikeMovies, recommend, genreMovies, API_URL }
}, { persist: true,})
