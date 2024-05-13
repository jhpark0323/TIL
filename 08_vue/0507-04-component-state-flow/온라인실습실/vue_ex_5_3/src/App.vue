<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList 
    @add-to-cart="addToCart"
    :products="products" 
    />
    <Cart
    v-if="cartList.length > 0"
    :cart-list="cartList"
    @remove-from-cart="removeFromCart"
    />
    <p v-if="cartList.length > 0">총 가격: {{ total }}원</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const cartList = ref([])

const addToCart = (name, price) => {
  cartList.value.push({ id: id++, name, price })
}

const removeFromCart = (cartId) => {
  console.log(cartId)
  const index = cartList.value.findIndex(cart => cart.id === cartId)
  if (index !== -1) {
    cartList.value.splice(index, 1)
  }
}

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const total = computed(() => {
  return cartList.value.reduce((acc, cur) => acc + cur.price, 0)
})

</script>
