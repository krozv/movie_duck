<template>
  <div>
    <NavBar />
  </div>
  <router-view></router-view>
</template>

<script setup>
import { RouterLink, RouterView} from 'vue-router'
import NavBar from './components/NavBar.vue';

</script>

<style lang='css'>
@import './assets/css/fonts.css';

</style>