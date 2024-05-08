<template>
<div>
<MainPage />

<RouterLink :to="{ name: 'some' }">Some</RouterLink> | 
<RouterLink :to="{ name: 'other' }">Other</RouterLink>
</div>
<RouterView />
</template>

<script setup>
import { ref } from 'vue'
import MainPage from './components/MainPage.vue'
</script>

<style scoped>

</style>