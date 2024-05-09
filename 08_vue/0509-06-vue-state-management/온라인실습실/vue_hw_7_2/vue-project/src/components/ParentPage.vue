<template>
  <div class="parent">
    <h3>부모 컴포넌트</h3>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
    v-for="child in family.children"
    :key="child.id"
    :child="child"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  family: Object
})

</script>

<style scoped>
.parent {
  border: solid 1px #CCCCCC;
  text-align: center;
  background-color: #f9f9f9;
  padding: 15px;
}
</style>