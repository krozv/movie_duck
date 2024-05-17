<template>
  <div class="loginpage">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="username">
        <label for="username">이메일</label>
        <input type="text" v-model.trim="username" id="username" placeholder="Email을 입력해주세요.">
      </div>
      <div class="password">
        <label for="password">패스워드</label>
        <input type="password" v-model.trim="password" id="password" placeholder="PW를 입력해주세요.">
      </div>
      <div class="submit">
      <input type="submit" value="로그인">
      </div>
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

  #password {
    border: 1px solid black;
    margin-left: 15px;
  }

  #username {
    border: 1px solid black;
    margin-left: 28px;
  }

  .username {
    text-align: start;
  }

  .password {
    text-align: start;
    margin-top: 10px;
  }

  .submit {
    border: 1px solid black;
    margin-top: 20px;
    width: 235px;
  }

  .login-form {
    margin-left: 30px;
  }
</style>
