<script setup >
import { RouterLink } from 'vue-router'
import Swal from 'sweetalert2'

import { AuthStore } from '@/stores/auth';
import { RetrieveUpdateDestroyMedicineUrl } from '@/endpoints';

const {medicines, highlight, query} = defineProps({
    medicines: Array,
    highlight: Boolean || null,
    query: String || null
})

const emits = defineEmits(['deleteMedicine'])
const store = AuthStore()

const deleteMedicine = id => {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
        }).then((result) => {
        if (result.isConfirmed) {
            fetch(RetrieveUpdateDestroyMedicineUrl + id + "/", {
                method: "DELETE",
                headers: {
                    "Authorization": `Token ${store.token}`
                }
            })
            .then(response =>  response.json())
            .then(data => {
                emits('deleteMedicine', id)
            })
        }
        });
}

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
    <th v-if="store.isAuthenticated" scope="col" >Actions</th>

    </tr>
</thead>
<tbody>
    <tr v-for="(medicine, index) in medicines"  :key="medicine.id">
    <th scope="row">{{ index + 1 }}</th>
    <td>
        <span v-if="highlight && query" :class="{highlight: highlight && medicine.name.toUpperCase().includes(query.toUpperCase())}" >{{ medicine.name }}</span>
        <span v-else>{{ medicine.name }}</span>
    </td>
    <td>
        <span v-if="highlight && query" :class="{highlight: highlight && medicine.generic.name.toString().toUpperCase().includes(query.toUpperCase())}" >{{ medicine.generic.name }}</span>
        <span v-else>{{ medicine.generic.name }}</span>
    </td>
    <td>{{ medicine.generic_unit }}</td>
    <td>{{ medicine.manufacturer.name }}</td>
    <td>{{ medicine.price }}</td>
    <td>{{medicine.no_of_tablets}}</td>
    <td>{{ medicine.batch_number }}</td>
    <td class="d-flex" v-if="store.isAuthenticated">
        <RouterLink :to="'/admin/update-medicine/' + medicine.id" >
            <img class="me-3" src="../assets/edit_note_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg" alt="edit">
        </RouterLink>
        <img @click="deleteMedicine(medicine.id)" :style="{cursor: 'pointer'}" src="../assets/delete_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg" alt="delete">
    </td>
    </tr>
</tbody>
</table>


</template>