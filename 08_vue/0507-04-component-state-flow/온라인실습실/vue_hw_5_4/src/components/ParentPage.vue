<template>
<div>
  <h1>부모 페이지입니다.</h1>
  <ChildPage
  @update-balance="updateBalance"
  v-for="child in children"
  :key="child.id"
  :my-prop="child"
  />
</div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from '@/components/ChildPage.vue'
  const children = ref([
    { name: '김하나', age: 30, balance: 1000000 },
    { name: '김두리', age: 20, balance: 10000 },
    { name: '김서이', age: 10, balance: 1000 },
  ])

  const updateBalance = (children) => {
    children.balance += 1000
    console.log(children)
    console.log('1')
  }

</script>

<style scoped>

</style>