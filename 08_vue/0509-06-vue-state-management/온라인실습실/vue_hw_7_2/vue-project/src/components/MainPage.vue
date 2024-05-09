<template>
<div>
<h1>pinia 연습하기</h1>
<ParentPage 
v-for="family in store.familyInfo"
:key="family.id"
:family="family"
/>
</div>
</template>

<script setup>
import { ref } from 'vue'
import ParentPage from '@/components/ParentPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

</script>

<style scoped>

</style>