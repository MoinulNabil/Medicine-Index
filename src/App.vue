<script setup>

import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue';

</script>

<template>
  <Navbar />
    <div class="container-fluid" >
      <RouterView />
    </div>
</template>

<style scoped>



</style>
