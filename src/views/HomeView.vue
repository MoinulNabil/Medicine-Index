<script setup>

document.title = "Home"

import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import { listMedicineUrl } from '@/endpoints';
import Loading from '@/components/Loading.vue';
import MedicineHome from '@/components/MedicineHome.vue';

const apiResponse = ref([])
const loading = ref(false)
const dataPerPage = ref(import.meta.env.VITE_APP_PAGESIZE)
const pages = ref(0)
const active = ref(1)
const searchBy = ref(null)
const router = useRouter()

const generatePages = (totalNumberOfData, dataPerPage) => {
  const number = totalNumberOfData / dataPerPage
  pages.value = Math.floor(number)
  if(totalNumberOfData % dataPerPage > 0) {
    pages.value += 1
  }
}

const navigate = page => {
  active.value = page
  getData(`${listMedicineUrl}?page=${page}`)
}

const getData = (url) => {
  loading.value = true
  fetch(url)
  .then(response => response.json())
  .then(data => {
    apiResponse.value = data
    generatePages(apiResponse.value.count, dataPerPage.value)
    loading.value = false
  })
}

const search = key => {
  key && router.push("/search" + "?q=" + key)
}

onMounted(() => {
  getData(listMedicineUrl)
})


</script>

<template>
    <div class="row mb-3">
      <div class="col-md-12 col-lg-12 ps-0">
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
      <div class="row mb-3 table-responsive">
      <div class="col-md-12 col-lg-12">
        <MedicineHome :medicines="apiResponse.results" />
      </div>
      </div>
    <div class="row">
      <div class="col-md-12 col-lg-12">
        <nav class="" aria-label="Page navigation example">
        <ul class="pagination">
          <li v-for="page in pages" :key="page" class="page-item" :class="{ active: page == active }">
            <button type="button" class="page-link" @click="navigate(page)">{{page}}</button>
          </li>
        </ul>
      </nav>
      </div>
    </div>
    </template>
</template>
