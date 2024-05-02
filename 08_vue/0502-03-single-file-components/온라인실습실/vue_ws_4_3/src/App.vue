<script setup>
import SingerDetail from './components/SingerDetail.vue';
import SingerList from './components/SingerList.vue';

</script>

<template>
  <SingerList />
  <h1 class="container">가수 목록</h1>
  <SingerDetail />
</template>

<style>
.container {
  display: flex; /* Flexbox 레이아웃을 사용합니다. */
  flex-direction: column; /* 세로 방향으로 아이템을 배치합니다. */
  align-items: center; /* 아이템을 수직 방향으로 가운데 정렬합니다. */
  text-align: center;
}

</style>
