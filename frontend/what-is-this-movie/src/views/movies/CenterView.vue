<template>
    <div class="px-4 mx-14">
        <v-carousel
    height="400"
    show-arrows="hover"
    cycle
    interval="4000"
    hide-delimiter-background
  >
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
      @click="goPage(i)"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
      >
        <div class="d-flex fill-height justify-center align-center">
          <div class="text-h2">
            {{ slide }} Slide
          </div>
        </div>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
    </div>
</template>

<script setup>
const colors = [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ]
const slides = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
import { useRouter } from 'vue-router'
const router = useRouter()
const goPage = function(num) {
    // 페이지 만든 거 넣기
    // router.push({ name: '' , params: { num: num }})
    console.log(num)
}

</script>



<style scoped>

</style>