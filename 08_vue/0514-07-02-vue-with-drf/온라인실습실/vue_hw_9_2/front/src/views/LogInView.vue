<template>
<div>
  <h1>로그인 페이지</h1>
  <form @submit.prevent="logIn">
    <label for="username">username : </label>
    <input type="text" id="username" v-model.trim="username">

    <label for="password">password : </label>
    <input type="password" id="password" v-model.trim="password">

    <input type="submit" value="submit">
  </form>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const username = ref(null)
const password = ref(null)
const store = useArticleStore()

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>