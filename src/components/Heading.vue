<script setup >

const {title} = defineProps({
    title: String
})


</script>

<template>

    <h2 class="mt-2 mb-4">{{ title }}</h2>

</template>