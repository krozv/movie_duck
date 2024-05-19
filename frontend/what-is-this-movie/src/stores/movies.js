import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useCounterStore } from './userStore'
import axios from 'axios'

export const useMovieStore = defineStore('movies', () => {
  const movie = ref([])
  const getMovies = function(movie_pk) {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/movie/${movie_pk}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(response => {
      movie.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
  }

  // juyeon
  const boxOfficeMovies = ref([])
  const store = useCounterStore()
  const boxOffice = function () {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/movie/boxoffice/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(response => {
      // console.log(response.data)
      boxOfficeMovies.value = response.data
      // console.log(boxOfficeMovies.value)
    })
    .catch(error => {
      console.log(error)
    })
  }
  return { movie, getMovies, boxOffice, boxOfficeMovies }
}, { persist: true,})
