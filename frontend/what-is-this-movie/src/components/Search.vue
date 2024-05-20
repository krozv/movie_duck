<template>
  <v-col cols="12">
    <v-form @submit.prevent="searchMovie">
      <v-text-field
        class="mx-auto"
        v-model="searchTerm"
        label="Search for a Movie"
        style="max-width: 350px"
        :prepend-inner-icon="mdiMagnify"
        rounded
        variant="solo-filled"
      ></v-text-field>
      <!-- <v-btn class="mt-2" type="submit" block>Submit</v-btn> -->
    </v-form>
  </v-col>
</template>

<script setup>
import { mdiMagnify } from '@mdi/js'
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const emit = defineEmits(['searchEmit'])

const router = useRouter();
const searchTerm = ref(null);

const searchMovie = () => {
  if (searchTerm.value.trim() !== '') {
    console.log(searchTerm.value.trim())
    emit("searchEmit", searchTerm.value)
    // 검색어가 비어 있지 않으면 검색 페이지로 이동
    router.push({ name: 'movie-search', params: { search: searchTerm.value } });
    
    // 검색 후 검색창 비우기
    searchTerm.value = '';
  }
};

</script>

<style scoped>

</style>