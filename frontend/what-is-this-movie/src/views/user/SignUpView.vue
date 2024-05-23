<template>
  <v-container class="d-flex justify-center">
    <div style="width: 70%; height: 500px" class="align-content-center">  
    <h3 class="text-center">Sign Up</h3>
      <v-form @submit.prevent="signUp">
        <v-text-field
          v-model.trim="username"
          :counter="10"
          label="username"
          required
        ></v-text-field>
        <v-text-field
        v-model.trim="password1"
        :counter="10"
        label="password1"
        type="password"
        required
        ></v-text-field>
        <v-text-field
        v-model.trim="password2"
        :counter="10"
        label="password2"
        type="password"
        required
        ></v-text-field>
        <v-btn
        class="mt-2"
        text="Submit"
        type="submit"
        block
      ></v-btn>
      </v-form>
    </div>
  </v-container>
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
</style>
