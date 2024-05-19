<template>
    <v-layout style="height: 45px">
        <v-app-bar :elevation="0" rounded >
            <div class="text-center">
                <p>HOME</p>
            </div>
            <template v-slot:append>
                <!-- 로그인이 됐으면 -->
                <div v-if="store.isLogin">
                    <v-btn v-tooltip:bottom="'log out'">
                    <router-link :to="{ name:'LogOutView'}">
                        <svg-icon type="mdi" :path="mdiLogout"
                        color=black
                        class="m-1"></svg-icon>
                    </router-link>
                    </v-btn>

                    <v-btn v-tooltip:bottom="'profile'">
                    <router-link :to="{ name:'Profile'}">
                        <svg-icon type="mdi" :path="mdiFaceMan"
                        color=black
                        class="m-1" 
                        ></svg-icon>
                    </router-link>
                    </v-btn>
                    
                </div>
                <div v-else>
                <!-- 로그인이 안됐으면 -->
                <v-btn v-tooltip:bottom="'sign up'">
                    <router-link :to="{ name:'SignUpView'}">
                        <svg-icon type="mdi" :path="mdiAccount"
                        color=black
                        class="m-1" 
                        ></svg-icon>
                    </router-link>
                </v-btn>

                <v-btn v-tooltip:bottom="'log in'">
                    <router-link :to="{ name:'LogInView'}">
                        <svg-icon type="mdi" :path="mdiLogin"
                        color=black
                        class="m-1" 
                        ></svg-icon>
                    </router-link>
                </v-btn>
                
                
                </div>
            </template>
        </v-app-bar>
    </v-layout>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useCounterStore } from '@/stores/userStore';
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiLogout, mdiFaceMan, mdiAccount, mdiLogin } from '@mdi/js'
const value = ref(1)

const router = useRouter();
const searchTerm = ref('');
const store = useCounterStore()

const searchMovie = () => {
    if (searchTerm.value.trim() !== '') {
        // 검색어가 비어 있지 않으면 검색 페이지로 이동
        router.push({ name: 'movie-search', params: { search: searchTerm.value } });
        // 검색 후 검색창 비우기
        searchTerm.value = '';
    }
};
</script>

<style scoped>

</style>