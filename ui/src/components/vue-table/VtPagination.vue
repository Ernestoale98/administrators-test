<template>
        <v-pagination
            v-if="props.totalPages>1"
                :length="props.totalPages"
                v-model="props.page"
                total-visible="10"
                color="primary"
                @input="page => props.setPage(page)"/>
</template>

<script>
    export default {
        name: "VtPagination",
        props: ['props']
    }
</script>