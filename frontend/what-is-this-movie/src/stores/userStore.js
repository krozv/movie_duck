import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('token') || null)
  const userData = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  // 서버로 요청을 보내고 응답 데이터 처리
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(response => {
      console.log(response)
      console.log(response.data)
      articles.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
  }
  
  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password1, password2 } = payload
    
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
    })
    .then((response) => {
      // console.log('회원가입 성공!')
      const password = password1
      logIn({ username, password })
    })
    .catch((error) => {
      console.log(error)
    })
  }
  
  const router = useRouter()
  
  const logIn = function(payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    
    // 2. axios로 django에 요청을 보냄
    axios({
      method:'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((response) => {
        console.log('로그인 완료')
        // 3. 로그인 성공 후 응답 받은 토큰 저장
        token.value = response.data.key
        localStorage.setItem('token', token.value)
        router.push({ name: 'home' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 로그아웃 구현
  const logout = () => {
    token.value = null
    const deleteItem = ['token', 'firstActor', 'secondActor', 'firstActorMovies', 
    'secondActorMovies', 'firstGenreMovies', 'secondGenreMovies', 'firstGenre', 
    'secondGenre', 'likedMovies', 'likeState'
  ]
    deleteItem.forEach((item) => {
      localStorage.removeItem(item)
    })
    router.push({ name: "home" });
  };
  
  const preLiked = ref([])
  
  // 유저 정보 받아오기
  const fetchUserData = () =>{
    // console.log(token.value)
    axios({
      method: 'get',
      url: `${API_URL}/accounts/users/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      // console.log(response.data)
      userData.value = response.data
      preLiked.value = userData.value.user_liked_movie
    })
    .catch((error) => {
      console.log(error)
    })
  }
  
  if (token.value) {
    fetchUserData()
  }
  
  // 좋아요 관련
  const likeStateKey = 'likeState';
  
  // 좋아요 상태 저장
  let likeState = JSON.parse(localStorage.getItem(likeStateKey)) || {}
  
  watch(preLiked, (newVal) => {
    if (preLiked.value) {
      preLiked.value.forEach((movie) => {
      likeState[movie.pk] = true;
      saveLikeState()
     })
    } 
  })
  // 특정 영화의 좋아요 상태를 토글하는 함수
  const toggleLike = (movieId) => {
    // 해당 영화의 좋아요 상태를 토글
    likeState[movieId] = !likeState[movieId];
    // 로컬 스토리지에 업데이트된 좋아요 상태 저장
    localStorage.setItem(likeStateKey, JSON.stringify(likeState));
  }

  // 특정 영화의 좋아요 상태를 가져오는 함수
  const getLikeState = (movieId) => {
    // 해당 영화의 좋아요 상태 반환
    return likeState[movieId] || false;
  }

  const initializeLikeState = () => {
    // 로컬 스토리지에서 좋아요 상태 초기화
    const storedLikeState = JSON.parse(localStorage.getItem('likeState')) || {};
    likeState = storedLikeState;
  }

  const saveLikeState = () => {
    // 로컬 스토리지에 좋아요 상태 저장
    localStorage.setItem('likeState', JSON.stringify(likeState));
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logout, userData, fetchUserData,
  toggleLike, getLikeState, initializeLikeState, saveLikeState }
}, { persist: true })
