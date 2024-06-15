<template>
  <div>
    <img
    width="100%"
    :aspect-ratio="1"
    :src="profileImg"
    class="img-setting mr-5"
    ></img>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  genre: String,
})


const profileImg = computed (() => {
  if ( props.genre ) {
    return new URL(`../assets/duck/${props.genre}.png`, import.meta.url).href
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