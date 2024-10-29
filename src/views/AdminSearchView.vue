<script setup >

    document.title = "Search"

    import { ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';

    import { searchMedicineUrl } from '@/endpoints';
    import Loading from '@/components/Loading.vue';
    import Heading from '@/components/Heading.vue';
    import Sidebar from '@/components/Sidebar.vue';
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

    const handleDelete = id => {
        medicines.value.data = medicines.value.data.filter(d => d.id != id)
    }

    onMounted(() => {
        getData(`${searchMedicineUrl}?q=${query.value}`)
    })

</script>

<template>

<div class="row">
    <Sidebar />
    <div class="col-md-12 col-lg-10 content">
        <Loading v-if="loading" />
        <template v-else >
            <h2 v-if="medicines.data && medicines.data.length > 0" class="my-3" > {{ medicines.data.length }} Results found for {{ medicines.q }}</h2>
            <MedicineList
            v-if="medicines.data && medicines.data.length > 0"
            @delete-medicine="(id) => handleDelete(id)"
            :medicines="medicines.data"
            :highlight="true"
            :query="medicines.q"
            />
            <h2 v-else >No medicines found with keyword {{ medicines.q }}</h2>        
        </template>
    
    </div>
</div>

</template>