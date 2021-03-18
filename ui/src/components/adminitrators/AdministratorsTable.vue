<template>
  <div>
    <v-breadcrumbs
        :items="items">
      <template v-slot:divider>
        <v-icon>mdi-chevron-right</v-icon>
      </template>
    </v-breadcrumbs>
  </div>
</template>

<script>
export default {
  name: "AdministratorsTable",
  data: () => ({
    items: [
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
  }),
}
</script>