<template>
  <div>
    <!-- {{ store.articles }} -->
    <ArticleListItem
      v-for="article in store.articles"
      :article="article"
    />
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
import ArticleListItem from './ArticleListItem.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>