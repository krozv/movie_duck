<template>
  <div class="loginpage">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">이메일 : </label>
        <input type="text" v-model.trim="username" id="username" placeholder="Email을 입력해주세요.">
      </div>
      <div>
        <label for="password">패스워드 : </label>
        <input type="password" v-model.trim="password" id="password" placeholder="PW를 입력해주세요.">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/userStore'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)

}
</script>

<style>
  .loginpage {
    text-align: center;
    margin-top: 10%;
    margin-left: 40%;
    width: 300px;
    height: 400px;
    display: block;
  }

  input #password {
    border: 1px solid black;
  }
</style>
