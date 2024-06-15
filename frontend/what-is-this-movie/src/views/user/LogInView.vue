<template>
  <v-container class="d-flex justify-center">
    <div style="width: 70%; height: 500px" class="align-content-center">  
    <h3 class="text-center">Log In</h3>
      <v-form @submit.prevent="logIn">
        <v-text-field
          v-model.trim="username"
          :counter="10"
          label="username"
          required
        ></v-text-field>
        <v-text-field
        v-model.trim="password"
        :counter="10"
        type="password"
        label="password"
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
</style>
