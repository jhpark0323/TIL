<template>
<div>
  <h1>회원 가입 페이지</h1>
  <form @submit.prevent="signUp">
    <label for="username">username : </label>
    <input type="text" id="username" v-model.trim="username">

    <label for="password1">password : </label>
    <input type="password" id="password1" v-model.trim="password1">

    <label for="password2">password Confirmation : </label>
    <input type="password" id="password2" v-model.trim="password2">

    <input type="submit" value="submit">
  </form>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles';
const store = useArticleStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  console.log(1)
  console.log(store)
  console.log(store.signUp)
  store.signUp(payload)
}

</script>

<style scoped>

</style>