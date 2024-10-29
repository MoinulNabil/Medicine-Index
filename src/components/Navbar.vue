<script setup >

import { RouterLink, useRouter } from 'vue-router'
import { AuthStore } from '@/stores/auth'

const store = AuthStore()
const router = useRouter()

const logout = () => {
  store.$reset();
  router.push("/login")
}

</script>

<template>

<nav class="navigationbar" id="navigationbar">
  <div class="container">
    <ul class="menu">
    <li class="menu-item">
        <RouterLink class="menu-link" to="/">Medicines</RouterLink>
    </li>
    <template v-if="store.isAuthenticated" >
      <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/dashboard">Dashboard</RouterLink>
        <span class="menu-link" :style="{cursor: 'pointer'}" @click="logout">Logout</span>
    </li>
    </template>
    <template v-else >
      <li class="menu-item">
        <RouterLink class="menu-link" to="/login">Login</RouterLink>
    </li>
    </template>
    
  </ul>
  </div>
</nav>

</template>