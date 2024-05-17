<template>
  <div class="loginpage">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="login-form">
      <div class="username">
        <label for="username">이메일</label>
        <input type="text" v-model.trim="username" id="username" placeholder="Email을 입력해주세요.">
      </div>
      <div class="password">
        <label for="password1">패스워드</label>
        <input type="password" v-model.trim="password1" id="password1" placeholder="PW를 입력해주세요.">
      </div>
      <div class="password">
        <label for="password2">패스워드 확인</label>
        <input type="password" v-model.trim="password2" id="password2" placeholder="PW를 입력해주세요.">
      </div>
      <div class="signup-submit">
      <input type="submit" value="회원가입">
    </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/userStore'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signUp = function () {
  if (password1.value !== password2.value) {
    console.log("Passwords do not match")
    return
  }
  
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
  .loginpage {
    text-align: center;
    margin-top: 10%;
    margin-left: 40%;
    width: 400px;
    height: 400px;
    display: block;
  }

  #username {
    border: 1px solid black;
    margin-left: 62px;
  }

  #password1 {
    border: 1px solid black;
    margin-left: 48px;
  }
  
  #password2 {
    border: 1px solid black;
    margin-left: 18px;
  }

  .signup-submit {
    border: 1px solid black;
    margin-top: 20px;
    width: 270px;
  }

  .login-form {
    margin-left: 50px;
    margin-top: 20px;
  }
</style>
