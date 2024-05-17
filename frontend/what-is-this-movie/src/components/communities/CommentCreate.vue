<template>
    <div class="comment-card">
      <form @submit.prevent="createArticle">
        <div>
          <textarea v-model.trim="content" id="content"></textarea>
          <input type="submit" value="제출" class="submit">
        </div>
    </form>

    </div>
</template>

<script setup>

</script>

<style scoped>
#content {
    border: 1px solid gray;
    width: 880px;
    height: 100px;
    margin: 20px;

}

.comment-card {
    display: flex;
    border: 1px solid gray;
    width: 1050px;
    height: 150px;
}
.submit {
    position: absolute;
    width: 100px;
    height: 100px;
    margin-top: 20px;
    border: 1px solid gray;
    
}
</style>