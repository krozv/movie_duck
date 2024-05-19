<template>
  <Navigation/>
  <!-- <div>
    <NavBar />
  </div> -->
  <router-view></router-view>
  <FooterComponent />
</template>

<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
import Navigation from '@/components/Navigation.vue'
import FooterComponent  from '@/components/Footer.vue'
</script>

<style>
@font-face {
    font-family: 'Apple';
    src: url('./assets/fonts/KoPubWorldDotumMedium.otf'),
      url('./assets/fonts/KoPubWorldDotumMedium.ttf');
    font-weight: 700;
    font-style: normal;
}

* {
  font-family:'Apple';
}
</style>