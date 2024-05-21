<template>
    <v-container>
      <v-row justify="space-between">
        <div style="display: flex; width: 100%;">
          <div v-if="!editAlert">
            {{ reply.content }}
          </div>
          <div v-else style="width: 100%;">
            <v-textarea @keyup.enter="[editAlert = !editAlert, editComment()]" v-model="reply.content"
              class="" rows="2" hide-details="true"
              ></v-textarea>
          </div>
        </div>
        <div justify="end" class="ml-auto">
          {{ reply.content.length }} / 300
          <div v-if="!editAlert">
            <svg-icon v-tooltip:bottom="'Reply'" @click="showReplies = !showReplies" type="mdi" :path="mdiCommentMultipleOutline" class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Edit'" v-if="!editAlert" @click="editAlert = !editAlert" type="mdi" :path="mdiCommentEditOutline"
              class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Delete'" v-if="!editAlert" @click="deleteAlert = true" type="mdi" :path="mdiCommentRemoveOutline" class="mx-1"></svg-icon>
          </div>
          <div v-else>
            <svg-icon v-tooltip:bottom="'Done'" @click="[editAlert = !editAlert, editComment()]" type="mdi" :path="mdiCommentCheckOutline"
            class="mx-1"></svg-icon>
            <svg-icon v-tooltip:bottom="'Reply'" @click="showReplies = !showReplies" type="mdi" :path="mdiCommentMultipleOutline" class="mx-1"></svg-icon>
          </div>
        </div>
      </v-row>
    </v-container>
  <hr>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiAlert, mdiCommentEditOutline, mdiCommentCheckOutline, mdiCommentRemoveOutline, mdiCommentMultipleOutline  } from '@mdi/js'

const props = defineProps({
  moviePk: Number,
  commentPk: Number,
})
</script>

<style scoped>

</style>