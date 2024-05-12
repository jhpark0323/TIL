<template>
  <ul>
    <ProductListItem
      @add-to-cart="addToCart(product)"
      v-for="product in products" 
      :key="product.id" 
      :product="product"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: Array
})

const emit = defineEmits(['addToCart'])

const addToCart = (product) => {
  emit('addToCart', product.name, product.price)
}

</script>
