<template>
<div style="border: 1px solid gray; padding: 0 10px; margin: 10px 0;">
  <h3>자식 페이지입니다.</h3>
  <p>{{ myProp.name }}</p>
  <p>{{ myProp.age }}</p>
</div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
  myProp: Object
})
</script>

<style scoped>

</style>