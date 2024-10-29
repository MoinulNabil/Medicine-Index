<script setup >

document.title = "Admin Login"

import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { AuthStore } from '@/stores/auth';
import { loginUrl } from '@/endpoints';
import Heading from '@/components/Heading.vue';

const email = ref("")
const password = ref("")
const errors = ref({})
const submitting = ref(false)
const store = AuthStore()
const router = useRouter()

async function handleSubmit() {
    errors.value = {}
    if(!email.value) {
        errors.value.email = "Email is required"
    }
    if(!password.value) {
        errors.value.password = "Password is required"
    }
    null
    if(Object.keys(errors.value).length ==0) {
        submitting.value = true
        const response = await fetch(loginUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({email: email.value, password: password.value})
        })
        if(response.ok) {
            const data = await response.json()
            store.setToken(data.token)
            email.value = ''
            password.value = null
            submitting.value = false
            router.push("admin/dashboard")
        }
        else {
            const data = await response.json()
            console.log(data)
            if(data.non_field_errors) {
                errors.value.server = data.non_field_errors.join()
            }
            submitting.value = false
        }

    }
}


</script>

<template>

    <div class="row justify-content-center">
        <div class="col-md-6 col-lg-8">
            <Heading title="Login to Admin Dashboard" />
            <hr />
            <form method="POST" @submit.prevent="handleSubmit" >
                <div class="form-group mb-3">
                    <p v-if="errors.server" class="text-danger" >{{ errors.server }}</p>
                </div>
                <div class="form-group mb-3">
                    <input class="form-control" type="email" v-model="email" placeholder="Enter email address">
                    <small v-if="errors.email" class="text-danger" >{{ errors.email }}</small>
                </div>
                <div class="form-group mb-3">
                    <input class="form-control" type="password" v-model="password" placeholder="Enter password">
                    <small v-if="errors.password" class="text-danger" >{{ errors.password }}</small>
                </div>
                <div class="form-group mb-3">
                    <button type="submit" class="btn btn-dark" :disabled="submitting" >
                        {{ submitting ? 'Authenticating.....': 'Login' }}
                    </button>
                </div>
                <div class="form-group mb-3 d-flex justify-content-center">
                    <p>
                        <strong>Email: </strong>nabil@gmail.com
                        <br>
                        <strong>Password: </strong>django
                    </p>
                </div>
            </form>
        </div>
    </div>


</template>