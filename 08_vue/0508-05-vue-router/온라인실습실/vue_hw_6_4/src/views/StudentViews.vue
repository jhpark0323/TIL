<template>
<div>
  <h1>학생 상세 정보 목록 입니다.</h1>
  <ul>
    <p v-for="student in students">
      <RouterLink style="text-decoration: none; color: black;"
      :to="{ name: 'detail', params: { 'name': student.name } }">
      {{ student.name }} 학생 정보 보기</RouterLink>
    </p>
  </ul>
</div>
</template>

<script setup>
import { ref } from 'vue'

const students = [
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' }
]

</script>

<style scoped>

</style>