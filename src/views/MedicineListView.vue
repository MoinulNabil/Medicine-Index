<script setup>

document.title = "Medicine List"

import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

import Swal from 'sweetalert2'

import { listMedicineUrl } from '@/endpoints';
import Loading from '@/components/Loading.vue';
import MedicineList from '@/components/MedicineList.vue';
import Sidebar from '@/components/Sidebar.vue';
import Heading from '@/components/Heading.vue';

const apiResponse = ref([])
const results = ref([])
const count = ref(0)
const loading = ref(false)
const dataPerPage = ref(import.meta.env.VITE_APP_PAGESIZE)

const pages = ref(0)
const active = ref(1)
const searchBy = ref(null)
const router = useRouter()
const route = useRoute()

const generatePages = (totalNumberOfData, dataPerPage) => {
  const number = totalNumberOfData / dataPerPage
  pages.value = Math.floor(number)
  if(totalNumberOfData % dataPerPage > 0) {
    pages.value += 1
  }
}

const navigate = page => {
  active.value = page
  const url = page != 1 ? `${listMedicineUrl}?page=${page}`: listMedicineUrl
  getData(url)
}

const getData = (url) => {
  loading.value = true
  fetch(url)
  .then(response => response.json())
  .then(data => {
    apiResponse.value = data
    results.value = data.results
    count.value = data.count
    generatePages(count.value, dataPerPage.value)
    loading.value = false
  })
}

const search = key => {
  key && router.push("/admin/search" + "?q=" + key)
}

const handleDelete = id => {
    results.value = results.value.filter(d => d.id != id)
    count.value -= 1
    generatePages(count.value, dataPerPage.value)
    if(results.value.length == 0) {
        if(pages.value === 1) {
            getData(listMedicineUrl + "?page=1")
        }
        if(apiResponse.value.previous) {
            getData(apiResponse.value.previous)
        }
        else if(apiResponse.value.next) {
            getData(apiResponse.value.next)
        }
    }
    Swal.fire({
      title: 'Medicine has been deleted successfully',
      icon: 'success',
      toast: true,
      showConfirmButton: false,
      position: "top-end",
      timer: import.meta.env.VITE_ALERT_TIMER
      })
}

onMounted(() => {
  getData(listMedicineUrl)
})


</script>

<template>
    <div class="row">
      <Sidebar />
      <div class="col-md-12 col-lg-10 content">
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
          <Heading :title="'Medicines (' + count + ')'" />
          <div class="col-md-12 col-lg-12">
            <MedicineList @delete-medicine="(id) => handleDelete(id)" :medicines="results" />
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
    </div>
  </div>
</template>
