<template>
<div>
  <h1>게시글 생성 페이지</h1>
  <form @submit.prevent="createArticle">
    <label for="title">제목 : </label>
    <input type="text" id="title" v-model.trim="title">
    <label for="content">내용 : </label>
    <input type="text" id="content" v-model.trim="content">
    <input type="submit" value="create">
  </form>
</div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useArticleStore } from '../stores/articles';

const store = useArticleStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
  })
    .then(() => {
      router.push({ name: 'home' })
    })
    .catch(error => console.log(error))
}

</script>

<style scoped>

</style>