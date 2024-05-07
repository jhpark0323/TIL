<template>
  <div>
    <li>
        <h4>{{ products.name }} - {{ products.price }}원</h4>
    </li>
  </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
    products: Object
})
</script>

<style scoped>

</style>