<template>
  <div class="child">
    <h4>자식 페이지</h4>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  child: Object
})

</script>

<style scoped>
.child {
  border: solid 1px #CCCCCC;
  text-align: center;
  background-color: white;
  padding: 15px;
  margin: 10px;
}
</style>