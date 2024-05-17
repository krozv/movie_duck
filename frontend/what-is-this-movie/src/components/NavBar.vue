<template>
    <div class="nav">
      <router-link :to="{ name:'home'}">Home </router-link>
      <span>|</span>
      <router-link :to="{ name:'movies'}">Movies</router-link>
      <span>|</span>
      <router-link :to="{ name:'recommended'}" class="mr-4">Recommend</router-link>
      <b-nav-form @submit.prevent="searchMovie"> 
        <b-form-input v-model="searchTerm" aria-label="Input" class="mr-1" @keyup.enter="searchMovie"></b-form-input>
        <img src="../assets/search.png" alt="#" @click="searchMovie">
      </b-nav-form> 
      <!-- 로그인이 됐으면 -->
      <div v-if="store.isLogin">
        <router-link :to="{ name:'LogOutView'}">로그아웃</router-link>
        <span>|</span>
        <router-link :to="{ name:'Profile'}">프로필</router-link>
      </div>
      <!-- 로그인이 안됐으면 -->
      <div v-else>
        <router-link :to="{ name:'SignUpView'}">회원가입</router-link>
        <span>|</span>
        <router-link :to="{ name:'LogInView'}">로그인</router-link>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  import { ref } from 'vue';
  import { useCounterStore } from '@/stores/userStore';
  
  const router = useRouter();
  const searchTerm = ref('');
  const store = useCounterStore()
  
  const searchMovie = () => {
    if (searchTerm.value.trim() !== '') {
      // 검색어가 비어 있지 않으면 검색 페이지로 이동
      router.push({ name: 'movie-search', params: { search: searchTerm.value } });
      // 검색 후 검색창 비우기
      searchTerm.value = '';
    }
  };
  </script>
  
  <style scoped>
  .nav {
    background-color: rgba(22, 21, 21, 0.8);
    height: 45px;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .glasses {
    margin-right: 50px;
  }
  
  a {
    color: rgba(255, 255, 255, 0.815);
    text-decoration-line: none;
    align-items: center;
  }
  
  span {
    margin: 10px;
  }
  
  button {
    width: 50px;
  }
  
  img {
    width: 30px;
  }
  </style>
  