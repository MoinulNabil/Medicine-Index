<script setup>

document.title = "Generic List"

import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import { AuthStore } from '@/stores/auth';
import { listCreateGenereicUrl } from '@/endpoints';
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
    results.value = data.results
    count.value = data.count
    loading.value = false
  })
}

const search = key => {
  key && router.push("/admin/search" + "?q=" + key)
}

onMounted(() => {
  getData(listCreateGenereicUrl)
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
        <Heading :title="'Generics (' + count + ')'" />  
        <div class="col-md-12 col-lg-12">
            <ul v-if="count > 0" class="list-group list-group-flush">
                <li v-for="generic in results" :key="generic.id" class="list-group-item ps-0">
                    {{ generic.name }}
                </li>
            </ul>
            <h2 v-else>No generics found</h2>
        </div>
      </div>
    </template>
      </div>
    </div>
</template>
