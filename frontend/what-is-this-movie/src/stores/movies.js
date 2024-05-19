import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useCounterStore } from './userStore'
import axios from 'axios'

export const useMovieStore = defineStore('movies', () => {
  const apiKey = import.meta.env.VITE_TMDB_API_KEY
  const movies = ref([])

  const getMovies = function() {
    axios({
      method: 'get',
      params: {page: '1'},
      url: "https://api.themoviedb.org/3/movie/top_rated?api_key=" + apiKey + "&language=ko-KR",
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
      console.log(response.data)
      boxOfficeMovies.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
  }
  return { movies, getMovies, boxOffice, boxOfficeMovies }
}, { persist: true,})
