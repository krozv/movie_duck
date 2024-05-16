<template>
    <div>
    <router-link :to="{ name:'home'}">Home</router-link> |
    <router-link :to="{ name:'movies'}">Movies</router-link> |
    <router-link :to="{ name:'review-search'}">Search</router-link> |
    <router-link :to="{ name:'recommended'}">Recommend</router-link> |
    <!-- 로그인이 됐으면 -->


    <!-- 로그인이 안됐으면 -->
    <router-link :to="{ name:'SignUpView'}">회원가입</router-link> |
    <router-link :to="{ name:'LogInView'}">로그인</router-link>
    </div>
</template>

<script setup>

</script>

<style scoped>
div {
    background-color: rgba(26, 24, 24, 0.8);
    height: 45px;
    text-align: center;
    
}

a {
    color: rgba(255, 255, 255, 0.815);
    text-decoration-line: none;
    align-items: center;
}
</style>