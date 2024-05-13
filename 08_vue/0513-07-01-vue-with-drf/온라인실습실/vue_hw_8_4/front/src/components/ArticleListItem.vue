<template>
<div>
  <h3>{{ store.articles.indexOf(article)+1 }}번 게시글</h3>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <hr>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '../stores/articles';
const store = useArticleStore()

defineProps({
  article: Object
})
// console.log(article)
</script>

<style scoped>

</style>