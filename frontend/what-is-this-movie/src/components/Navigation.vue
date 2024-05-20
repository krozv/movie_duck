<template>
    <v-layout style="height: 50px">
        <v-app-bar :elevation="0" rounded style="height: 50px">
            <!-- 반응형 추가하기 -->
            <v-row>
                <v-col cols="4" offset="4" class="p-1">
                <div class="d-flex justify-center">
                    <router-link :to="{ name:'home'}">
                        <button>
                        <img 
                        src="../assets/logo_size.png" 
                        alt="logo"
                        height="50px">
                        </button>
                        <!-- <span>test</span> -->
                    </router-link>
                </div>
                </v-col>
                <v-col>
                <!-- 로그인이 됐으면 -->
                <div 
                    class="d-flex justify-end"
                    v-if="store.isLogin" style="height: 50px" >
                    <v-btn>
                    <router-link :to="{ name:'recommend'}">
                        <svg-icon type="mdi" :path="mdiMovieSearch"
                        color=black
                        class="m-1"></svg-icon>
                    </router-link>
                    </v-btn>
                    <v-btn v-tooltip:bottom="'log out'" >
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
                <div 
                    v-else
                    class="d-flex justify-end">
                <!-- 로그인이 안됐으면 -->
                <v-btn>
                        <svg-icon type="mdi" :path="mdiMovieSearch"
                        color=black
                        class="m-1"></svg-icon>
                    </v-btn>
                
                <v-btn v-tooltip:bottom="'log in'">
                    <router-link :to="{ name:'LogInView'}">
                        <svg-icon type="mdi" :path="mdiLogin"
                        color=black
                        class="m-1" 
                        ></svg-icon>
                    </router-link>
                </v-btn>
                <v-btn v-tooltip:bottom="'sign up'">
                    <router-link :to="{ name:'SignUpView'}">
                        <svg-icon type="mdi" :path="mdiAccount"
                        color=black
                        class="m-1" 
                        ></svg-icon>
                    </router-link>
                </v-btn>

                </div>
                </v-col>
            </v-row>
        </v-app-bar>
    </v-layout>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useCounterStore } from '@/stores/userStore';
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiLogout, mdiFaceMan, mdiAccount, mdiLogin, mdiMovieSearch } from '@mdi/js'

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