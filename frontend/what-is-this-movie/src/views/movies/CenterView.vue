<template>
  <div class="px-4 mx-14">
    <v-carousel max-width="700px" height="100%" show-arrows="hover" cycle interval="6000" hide-delimiter-background>
      <v-carousel-item v-for="(slide, i) in slides" :key="i" @click="goPage(i)">
        <v-sheet v-tooltip:top=list[i]>
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
  new URL('@/assets/background/duck_bg.png', import.meta.url).href,
  new URL('@/assets/background/duck_bg2.png', import.meta.url).href,
])
const slides = ['First', 'Second']
import { useRouter } from 'vue-router'
const router = useRouter()
const list = ['recommend', 'Profile']
const goPage = function(i) {
    router.push({name: list[i]})
}
</script>



<style scoped>
.slide{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>