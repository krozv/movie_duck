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

<style>
@font-face {
    font-family: 'Apple';
    src: url('./assets/fonts/AppleSDGothicNeoM.ttf') format('truetype');
    font-weight: 700;
    font-style: normal;
}

* {
  font-family:'Apple';
}
</style>