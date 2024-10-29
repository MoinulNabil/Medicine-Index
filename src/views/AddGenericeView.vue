<script setup >

document.title = "Add Generic"

import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Swal from "sweetalert2"

import { AuthStore } from '@/stores/auth';
import Heading from '@/components/Heading.vue';
import Sidebar from '@/components/Sidebar.vue';
import { listCreateGenereicUrl } from '@/endpoints';

const name = ref('')
const errors = ref({})
const submitting = ref(false)
const store = AuthStore()
const router = useRouter()
const route = useRoute()

async function handleSubmit() {
    errors.value = {}
    if(!name.value) {
        errors.value.name = "Name is required"
    }
    if(Object.keys(errors.value).length ==0) {
        submitting.value = true
        const request = await fetch(listCreateGenereicUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${store.token}`
            },
            body: JSON.stringify({name: name.value})
        })
        if(!request.ok) {
            const response = await request.json()
            errors.value = {}
            errors.value.name = response.name.join()
            submitting.value = false
        }
        else {
            const response = await request.json()
            name.value = ''
            submitting.value = false
            Swal.fire({
                title: 'New generic has been added successfully',
                icon: 'success',
                toast: true,
                showConfirmButton: false,
                position: "top-end",
                timer: import.meta.env.VITE_ALERT_TIMER
                })
                const redirect_url = route.query.redirect

                if(redirect_url) {
                    router.push(redirect_url)
                }
        }
    }
}


</script>

<template>

    <div class="row justify-content-center">
        <Sidebar />
        <div class="col-md-12 col-lg-10 px-4 content">
            <Heading title="Add Generic" />
            <hr />
            <form method="POST" @submit.prevent="handleSubmit" >
                <div class="form-group mb-3">
                    <p v-if="errors.server" class="text-danger" >{{ errors.server }}</p>
                </div>
                <div class="form-group mb-3">
                    <input class="form-control" type="text" v-model="name" placeholder="Enter generic name">
                    <small v-if="errors.name" class="text-danger" >{{ errors.name }}</small>
                </div>
                <div class="form-group mb-3">
                    <button type="submit" class="btn btn-dark" :disabled="submitting" >
                        {{ submitting ? 'Adding.....': 'Add' }}
                    </button>
                </div>
            </form>
        </div>
    </div>


</template>