<script setup >

document.title = "Dashboard"

import { ref, onMounted } from 'vue';
import { useRouter, RouterLink } from 'vue-router';

import { AuthStore } from '@/stores/auth';
import { getDashboardData } from '@/endpoints';

import Loading from '@/components/Loading.vue';
import Sidebar from '@/components/Sidebar.vue';
import Heading from '@/components/Heading.vue';

const apiResponse = ref([])
const results = ref([])
const count = ref(0)
const loading = ref(false)

const searchBy = ref(null)
const router = useRouter()
const store = AuthStore()


const getData = (url) => {
  loading.value = true
  fetch(url, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${store.token}`
    }
  })
  .then(response => response.json())
  .then(data => {
    apiResponse.value = data
    loading.value = false
  })
}

const search = key => {
  key && router.push("/admin/search" + "?q=" + key)
}

onMounted(() => {
  getData(getDashboardData)
})

</script>


<template>

<div class="row">
      <Sidebar />
      <div class="col-md-12 col-lg-10 content">
        <div class="row mb-3">
      <div class="col-md-12 col-lg-12">
        <form method="POST" @submit.prevent="search(searchBy)" >
          <div class="form-group d-flex" >
            <input class="form-control me-2" v-model="searchBy"  placeholder="Search by medicine or generic name"/>
            <button type="submit" class="btn btn-dark px-3">Search</button>
          </div>
        </form>
      </div>
    </div>
    <Loading v-if="loading" />
    <template v-else >
      <div class="row mb-3">
        <div class="col-md-12 col-lg-12 mt-3">
            <div class="row">
                <div class="col-md-4 col-lg-4 mb-3">
                    <div class="card">
                        <div class="card-header fw-bold text-center">
                            Total Brands
                        </div>
                        <div class="card-body text-center">
                            <h5 class="card-title">Number of Manufacturers</h5>
                            <p class="display-6 mb-2">{{ apiResponse.manufacturers }}</p>
                            <RouterLink to="/admin/manufacturer-list" class="btn btn-dark mt-3">View All</RouterLink>
                        </div>
                        </div>
                </div>
                <div class="col-md-4 col-lg-4 mb-3">
                    <div class="card">
                        <div class="card-header fw-bold text-center">
                            Total Brands
                        </div>
                        <div class="card-body text-center">
                            <h5 class="card-title">Number of Generics</h5>
                            <p class="display-6 mb-2">{{ apiResponse.generics }}</p>
                            <RouterLink to="/admin/generic-list" class="btn btn-dark mt-3">View All</RouterLink>
                        </div>
                        </div>
                </div>
                <div class="col-md-4 col-lg-4 mb-3">
                    <div class="card">
                        <div class="card-header fw-bold text-center">
                            Total Brands
                        </div>
                        <div class="card-body text-center">
                            <h5 class="card-title">Number of Medicines</h5>
                            <p class="display-6 mb-2">{{ apiResponse.medicines }}</p>
                            <RouterLink to="/admin/medicine-list" class="btn btn-dark mt-3">View All</RouterLink>
                        </div>
                        </div>
                </div>
            </div>
        </div>
      </div>
    </template>
      </div>
    </div>

</template>