<template>
  <div>
    <p class='greeting'>{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello')
</script>

<style scoped>
.greeting {
  color: crimson;
}
</style>
