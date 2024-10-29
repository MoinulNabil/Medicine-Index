<script setup >

    document.title = "Search"

    import { ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';

    import { searchMedicineUrl } from '@/endpoints';
    import Loading from '@/components/Loading.vue';
    import Heading from '@/components/Heading.vue';
    import MedicineList from '@/components/MedicineList.vue';

    const route = useRoute()
    const query = ref(route.query.q)
    const medicines = ref({})
    const loading = ref(false)

    const getData = (url) => {
        loading.value = true
        fetch(url)
        .then(response => response.json())
        .then(data => {
            medicines.value = data
            loading.value = false
        })
    }

    onMounted(() => {
        getData(`${searchMedicineUrl}?q=${query.value}`)
    })

</script>

<template>

<div class="row">
    <div class="col-md-12 col-lg-12">
        <Loading v-if="loading" />
        <template v-else >
            <h2 class="my-3" >Results for {{ medicines.q }}</h2>
            <MedicineList 
            v-if="medicines.data && medicines.data.length > 0"
            :medicines="medicines.data"
            :highlight="true"
            :query="medicines.q"
            />
            <h2 v-else >No medicines found with keyword {{ medicines.q }}</h2>        
        </template>
    
    </div>
</div>

</template>