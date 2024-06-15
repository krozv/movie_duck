<template>
    <v-layout style="height: 50px">
        <v-app-bar :elevation="0" rounded style="height: 50px">
            <!-- 반응형 추가하기 -->
            <v-row>
                <v-col cols-md="4" offset-md="4" class="p-1">
                <div class="d-flex justify-content-md-center px-1">
                    <!-- <router-link :to="{ name:'home'}"> -->
                        <div v-tooltip:bottom="'Home'" @click="goHome">
                        <img
                        class="home"
                        src="../assets/logo_size.png" 
                        alt="logo"
                        height="50px">
                        </div>
                </div>
                </v-col>
                <v-col>
                <!-- 로그인이 됐으면 -->
                <div 
                    class="d-flex justify-end"
                    v-if="store.isLogin" style="height: 50px" >
                    <v-btn v-tooltip:bottom="'Recommend'">
                    <router-link :to="{ name:'recommend'}">
                        <svg-icon type="mdi" :path="mdiMovieSearch"
                        color=black
                        class=""></svg-icon>
                    </router-link>
                    </v-btn>
                    <v-btn v-tooltip:bottom="'Log out'" >
                    <router-link :to="{ name:'LogOutView'}">
                        <svg-icon type="mdi" :path="mdiLogout"
                        color=black
                        class=""></svg-icon>
                    </router-link>
                    </v-btn>

                    <v-btn v-tooltip:bottom="'Profile'">
                    <router-link :to="{ name:'Profile'}">
                        <svg-icon type="mdi" :path="mdiFaceMan"
                        color=black
                        class="" 
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

const goHome = function () {
    router.push({ name: 'home'})
}
</script>

<style scoped>
.home:hover {
    background-color:#ededed;
    transition: 0.7s;
    border-radius: 100% 100%;
}
</style>