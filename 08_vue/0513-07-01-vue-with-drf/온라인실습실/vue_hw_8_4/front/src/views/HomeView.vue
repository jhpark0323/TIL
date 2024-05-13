<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{name: 'CreateView'}">
      [게시글 생성]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '../components/ArticleList.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '../stores/articles';
import { RouterLink } from 'vue-router';

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style lang="scss" scoped>

</style>