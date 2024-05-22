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
import { computed } from 'vue'

const props = defineProps({
  Genre: String,
})


const profileImg = computed (() => {
  if ( props.Genre ) {
    return new URL(`../assets/duck/${props.Genre}.png`, import.meta.url).href
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