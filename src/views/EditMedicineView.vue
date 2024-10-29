<script setup >

document.title = "Edit Medicine"

import { ref, onMounted } from 'vue';
import { RouterLink, useRoute } from 'vue-router'

import Swal from "sweetalert2"

import { AuthStore } from '@/stores/auth';
import Heading from '@/components/Heading.vue'
import Sidebar from '@/components/Sidebar.vue'
import Loading from '@/components/Loading.vue'
import { RetrieveUpdateDestroyMedicineUrl, fetchGenericAndManufactuerUrl } from '@/endpoints';

const genericList = ref([])
const manufacturerList = ref([])

const manufacturer = ref(null)
const generic = ref()
const generic_unit = ref()
const name = ref()
const no_of_tablets = ref()
const price = ref()
const batch_number = ref()
const description = ref()
const errors = ref({})
const submitting = ref(false)
const store = AuthStore()
const route = useRoute()
const loading = ref(false)
const medicine_object = ref({})


const getGenericAndManufactuerData = () => {
    loading.value = true
    fetch(fetchGenericAndManufactuerUrl, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${store.token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        genericList.value = data.generics
        manufacturerList.value = data.manufacturers
        if(genericList.value[0].id) {
            generic.value = genericList.value[0].id
        }
        if(manufacturerList.value[0].id) {
            manufacturer.value = manufacturerList.value[0].id
        }
        loading.value = false
    })
}

const getMedicine = (id) => {
    loading.value = true
    fetch(RetrieveUpdateDestroyMedicineUrl + id + "/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${store.token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        manufacturer.value = data.manufacturer.id
        generic.value = data.generic.id
        generic_unit.value = data.generic_unit
        name.value = data.name
        no_of_tablets.value = data.no_of_tablets
        price.value = data.price
        batch_number.value = data.batch_number
        description.value = data.description
        medicine_object.value = data
        loading.value = false
    })
}


const validate = data => {
    errors.value = {}
    Object.keys(data).forEach(key => {
        if(!data[key]) {
            errors.value[key] = key + " is required";
        }
    })
}

async function handleSubmit() {
    const payload = {
        manufacturer: manufacturer.value,
        generic: generic.value,
        name: name.value,
        generic_unit: generic_unit.value,
        no_of_tablets: no_of_tablets.value,
        price: price.value,
        batch_number: batch_number.value,
        description: description.value
        }
    validate(payload)
    if(Object.keys(errors.value).length ==0) {
        submitting.value = true
        const request = await fetch(RetrieveUpdateDestroyMedicineUrl + route.params.id + "/", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${store.token}`
            },
            body: JSON.stringify(payload)
        })
        if(!request.ok) {
            const response = await request.json()
            errors.value = {}
            // Handle server errors
            submitting.value = false
        }
        else {
            const response = await request.json()
            submitting.value = false
            Swal.fire({
                title: 'Medicine has been updated successfully',
                icon: 'success',
                toast: true,
                showConfirmButton: false,
                position: "top-end",
                timer: import.meta.env.VITE_ALERT_TIMER
                })
            submitting.value = false
        }
        
    }
}


onMounted(() => {
    getGenericAndManufactuerData()
    getMedicine(route.params.id)
})


</script>

<template>
    <Loading v-if="loading" />
    <div v-else class="row justify-content-center">
        <Sidebar />
        <div class="col-md-12 col-lg-10 px-4 content">
            <Heading :title="'Update ' + medicine_object.name + ' ' + medicine_object.generic_unit " />
            <hr />
            <form method="POST" @submit.prevent="handleSubmit(event)" >
                <div class="form-group mb-3">
                    <p v-if="errors.server" class="text-danger" >{{ errors.server }}</p>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Select Manufacturer<span class="text-danger" > *</span>
                        <RouterLink to="/admin/add-manufacturer?redirect=/admin/add-medicine" >
                            <img src="../assets/add_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg" alt="add">
                        </RouterLink>
                </p>
                    <select class="form-control" v-model="manufacturer">
                        <option v-for="(manufacturer, index) in manufacturerList" :key="manufacturer.id" :value="manufacturer.id" >{{ manufacturer.name }}</option>
                    </select>
                    <small v-if="errors.manufacturer" class="text-danger" >{{ errors.manufacturer }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Select Generic<span class="text-danger" > *</span></p>
                    <select class="form-control" v-model="generic">
                        <option v-for="(generic, index)  in genericList" :key="generic.id" :value="generic.id" >{{ generic.name }}</option>
                    </select>
                    <small v-if="errors.generic" class="text-danger" >{{ errors.generic }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Medicine Name<span class="text-danger" > *</span></p>
                    <input class="form-control" type="text" v-model="name" placeholder="Enter generic name">
                    <small v-if="errors.name" class="text-danger" >{{ errors.name }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Generic Unit<span class="text-danger" > *</span></p>
                    <input class="form-control" type="text" v-model="generic_unit" placeholder="Enter generic unit in grams">
                    <small v-if="errors.generic_unit" class="text-danger" >{{ errors.generic_unit }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">No of Tablets<span class="text-danger" > *</span></p>
                    <input class="form-control" type="text" v-model="no_of_tablets" placeholder="No of Tablets in a Strip">
                    <small v-if="errors.no_of_tablets" class="text-danger" >{{ errors.no_of_tablets }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Price<span class="text-danger" > *</span></p>
                    <input class="form-control" type="text" v-model="price" placeholder="Enter price">
                    <small v-if="errors.price" class="text-danger" >{{ errors.price }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Batch No<span class="text-danger" > *</span></p>
                    <input class="form-control" type="text" v-model="batch_number" placeholder="Enter batch number">
                    <small v-if="errors.batch_number" class="text-danger" >{{ errors.batch_number }}</small>
                </div>
                <div class="form-group mb-3">
                    <p class="mb-2">Description<span class="text-danger" > *</span></p>
                    <textarea class="form-control" type="text" v-model="description" />
                    <small v-if="errors.description" class="text-danger" >{{ errors.description }}</small>
                </div>
                <div class="form-group mb-3">
                    <button type="submit" class="btn btn-dark" :disabled="submitting">
                        {{ submitting ? 'Updating.....': 'Update' }}
                    </button>
                </div>
            </form>
        </div>
    </div>


</template>