<template>
    <div>
    <router-link :to="{ name:'home'}">Home </router-link><span>|</span>
    <router-link :to="{ name:'movies'}"> Movies</router-link><span>|</span>
    <router-link :to="{ name:'review-search'}">Search</router-link><span>|</span>
    <router-link :to="{ name:'recommended'}">Recommend</router-link><span>|</span>
    <!-- 로그인이 됐으면 -->


    <!-- 로그인이 안됐으면 -->
    <router-link :to="{ name:'SignUpView'}">회원가입</router-link><span>|</span>
    <router-link :to="{ name:'LogInView'}">로그인</router-link>
    </div>
</template>

<script setup>

</script>

<style scoped>
div {
    background-color: rgba(22, 21, 21, 0.8);
    height: 45px;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    
}

a {
    color: rgba(255, 255, 255, 0.815);
    text-decoration-line: none;
    align-items: center;
}

span {
    margin: 10px;
}
</style>