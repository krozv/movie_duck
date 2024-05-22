<template>
    <!-- 단일 영화 컴포넌트 -->
    <!-- <div @click="storeMovie" :class="{ 'border-warning': clickCard }" class="card text-bg-dark" style="height: 100%;">
        <img class="card-img" 
            :src="'https://image.tmdb.org/t/p/w300'+moviePosterPath" 
            alt="Card image cap"
            style="height: 100%;">
        <div class="card-img-overlay">
            <h4 class="card-title fw-bold  text-dark highlight" 
            :class="{ 'text-warning': clickCard }">{{ movieTitle }}</h4>
        </div>
    </div> -->
    <v-hover v-slot="{ isHovering, props }">
      <v-card
        @click="storeMovie" 
        :class="{'click-event': clickCard, 'on-hover': !isHovering,  }"
        :elevation="isHovering ? 12 : 2"
        style="height: 100%;"
        v-bind="props"
      >
        <v-img
        :src="'https://image.tmdb.org/t/p/w300'+moviePosterPath" 
        alt="Card image cap"
        style="height: 100%;"
        cover
        >
        </v-img>
      </v-card>
    </v-hover>
</template>

<script setup>
import 'bootstrap'
import { ref } from 'vue';

const props = defineProps({
    movieId: Number,
    movieTitle: String,
    moviePosterPath: String,
})

const emits = defineEmits([
    'clickEvent',
])

const clickCard = ref(false)

const storeMovie = function() {
    emits('clickEvent', props.movieId)
    clickCard.value = !clickCard.value
}
</script>

<style scoped>
.v-card {
    transition: opacity .4s ease-in-out;
  }

.on-hover {
    opacity: 0.6;
}
.click-event {
    opacity: 1;
}
</style>