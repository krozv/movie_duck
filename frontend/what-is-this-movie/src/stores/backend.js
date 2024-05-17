import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// 나중에 쓸 일 있으면 아래 수정할 것임
export const useMovieStore = defineStore('movies', () => {
  const movies = ref([])

  const sendMovies = function() {
    axios({
     }
    )
    .then((response) => {
      movies.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // juyeon
  const userLikeMovies = ref([])
  return { sendMovies }
}, { persist: true,})
