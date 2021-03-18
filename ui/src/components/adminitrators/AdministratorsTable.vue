<template>
  <v-container>
    <v-breadcrumbs
        :items="breadcrumbs">
      <template v-slot:divider>
        <v-icon>mdi-chevron-right</v-icon>
      </template>
    </v-breadcrumbs>
    <div id="people">
      <v-server-table url="/people" :columns="columns" :options="options"/>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "AdministratorsTable",
  data: () => ({
    breadcrumbs: [
      {
        text: 'Inicio',
        disabled: false,
        href: 'breadcrumbs_dashboard',
      },
      {
        text: 'Administradores',
        disabled: false,
        href: 'breadcrumbs_link_1',
      }
    ],
    columns: ['id', 'name', 'age'],
    options: {
      // see the options API
    }
  }),
}
</script>