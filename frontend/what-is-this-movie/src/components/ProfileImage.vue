<template>
  <div>
    <img
    width="100"
    :aspect-ratio="1"
    :src="profileImg"
    class="img-setting mr-5"
    ></img>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  firstGenre: String,
})


const profileImg = computed (() => {
  if ( props.firstGenre ) {
    return new URL(`../assets/duck/${props.firstGenre}.png`, import.meta.url).href
  } else {
    return new URL(`../assets/duck/default.png`, import.meta.url).href
  }
})


</script>

<style scoped>
.img-setting {
  border-radius: 100% 100%;
}
</style>