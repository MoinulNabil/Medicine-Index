<script setup >

import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const show = ref(false)

const toggle = () => {
    console.log('to')
    const open = show.value
    console.log(open)
    show.value = open ? false: true
    console.log(show.value)
}

</script>

<template>
<div class="sidebar-toggle" @click="toggle" id="sidebar-toggle" >
    <img src="../assets/legend_toggle_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg" alt="Toggle">
</div>
<div class="col-md-12 col-lg-2 px-4 mb-5 sidebar-col" :class="{'show': show}" id="sidebar-col">
  <aside class="sidebar" id="sidebar">
    <ul class="menu p-md-0 p-sm-0">
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/dashboard">Dashboard</RouterLink>
    </li>
    <hr>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/medicine-list">Medicine List</RouterLink>
    </li>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/add-medicine">Add Medicine</RouterLink>
    </li>
    <hr>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/generic-list">Generic List</RouterLink>
    </li>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/add-generic">Add Generic</RouterLink>
    </li>
    <hr>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/manufacturer-list">Manufacturer List</RouterLink>
    </li>
    <li class="menu-item">
        <RouterLink class="menu-link" to="/admin/add-manufacturer">Add Manufactuer</RouterLink>
    </li>
  </ul>
</aside>
</div>

</template>