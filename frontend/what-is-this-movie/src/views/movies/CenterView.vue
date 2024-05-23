<template>
  <div class="px-4 mx-14">
    <v-carousel max-width="700px" height="100%" show-arrows="hover" cycle interval="6000" hide-delimiter-background>
      <v-carousel-item v-for="(slide, i) in slides" :key="i" @click="goPage()">
        <v-sheet>
          <img 
          :src=bgImg[i] class="slide">

        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const bgImg = ref([
  new URL('@/assets/background/duck_bg1.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg2.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg3.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg4.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg5.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg6.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg7.png', import.meta.url).href,
])
const slides = ['1', '2', '3', '4','5','6','7']
import { useRouter } from 'vue-router'
const router = useRouter()
const goPage = function() {
    router.push({name: 'recommend'})
}
</script>



<style scoped>
.slide{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>