<template>
  <header>
    <div class="wrapper">
      <MainPage />
      <nav>
        <RouterLink :to="{name: 'some'}">Some</RouterLink> | 
        <RouterLink :to="{name: 'other'}">Other</RouterLink> |
        <RouterLink :to="{name: 'students'}">Students</RouterLink>

        <!-- <RouterLink to="/"></RouterLink> -->
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'

</script>

<style scoped>

</style>
