<template>
    
    <v-app>
        <v-container>
            <v-footer color="white">
                <v-row justify="center" no-gutters>
                    
                    <v-col class="text-center mt-4" cols="12">
                        <v-row justify="center" class="m-2">
                        <span>소개를 잘 적어봅시다.</span>
                        </v-row>
                        <v-row justify="center" class="m-2">
                        <a href="https://github.com/krozv/ssafy_final_pjt">
                        <svg-icon type="mdi" :path="mdiGithub"></svg-icon>
                        </a>
                        <span>
                        &nbsp; © &nbsp;{{ new Date().getFullYear() }} 
                        </span>
                        </v-row>
                    </v-col>
                </v-row>
            </v-footer>
        </v-container>
    </v-app>
</template>

<script setup>
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiGithub } from '@mdi/js'
</script>

<style scoped>
a {
    color: black
}
a:link {
    color : black
}
a:hover {
    color: #c0c0c0
}
</style>