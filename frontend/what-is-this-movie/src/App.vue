<template>
  <nav>
    <Navigation/>
  </nav>
  <main>
    <router-view></router-view>
  </main>
  <footer>
    <FooterComponent />
  </footer>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'
import Navigation from '@/components/Navigation.vue'
import FooterComponent  from '@/components/Footer.vue'
import { useMovieStore } from '@/stores/movies';

const store = useMovieStore();
onMounted(() => {
  store.getAllMovies();
  console.log('앱 구동')
});

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

main{
  background-color: #e4e4e4f9;
}
</style>