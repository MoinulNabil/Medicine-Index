<script setup >

import { AuthStore } from '@/stores/auth';

const {medicines, highlight, query} = defineProps({
    medicines: Array,
    highlight: Boolean || null,
    query: String || null
})

</script>


<template>

<table class="table">
<thead>
    <tr>
    <th scope="col">Serial</th>
    <th scope="col">Name</th>
    <th scope="col">Generic</th>
    <th scope="col">Unit</th>
    <th scope="col">Manufactuer</th>
    <th scope="col">Price</th>
    <th scope="col">Tablets</th>
    <th scope="col">Batch No</th>

    </tr>
</thead>
<tbody>
    <tr v-for="(medicine, index) in medicines"  :key="medicine.id">
    <th scope="row">{{ index + 1 }}</th>
    <td>
        <span v-if="highlight && query" :class="{highlight: highlight && medicine.name.includes(query)}" >{{ medicine.name }}</span>
        <span v-else>{{ medicine.name }}</span>
    </td>
    <td>
        <span v-if="highlight && query" :class="{highlight: highlight && medicine.generic.name.toString().includes(query)}" >{{ medicine.generic.name }}</span>
        <span v-else>{{ medicine.generic.name }}</span>
    </td>
    <td>{{ medicine.generic_unit }}</td>
    <td>{{ medicine.manufacturer.name }}</td>
    <td>{{ medicine.price }}</td>
    <td>{{medicine.no_of_tablets}}</td>
    <td>{{ medicine.batch_number }}</td>
    </tr>
</tbody>
</table>


</template>