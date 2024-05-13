<template>
  <div>
    <h2>장바구니</h2>
    <ul>
      <li v-for="cart in cartList" :key="cart.id">
        {{ cart.name }} - {{ cart.price }}원
        <button @click="removeFromCart(cart.id)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  cartList: Array
})

const emit = defineEmits(['remove-from-cart'])

const removeFromCart = (cartId) => {
  emit('remove-from-cart', cartId)
}

</script>


<style scoped>

</style>