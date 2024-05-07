<template>
<div>
  <h3>자식 페이지입니다.</h3>
  <p>이름 : {{ myProp.name }}</p>
  <p>나이 : {{ myProp.age }}</p>
  <p>용돈 : {{ myProp.balance }}</p>
  <button @click="giveMeAllowance(myProp)">용돈 주세요.</button>
</div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
  myProp: Object
})

const emit = defineEmits(['updateBalance'])

const giveMeAllowance = (children) => {
  emit('updateBalance', children)
}

</script>

<style scoped>

</style>