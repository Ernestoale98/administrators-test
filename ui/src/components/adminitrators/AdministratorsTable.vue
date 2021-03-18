<template>
  <v-container>
    <v-breadcrumbs
        :items="breadcrumbs">
      <template v-slot:divider>
        <v-icon>mdi-chevron-right</v-icon>
      </template>
    </v-breadcrumbs>
    <div id="people">
      <v-server-table url="administrators" :columns="columns" :options="options">
        <div :slot="`filter__${filter}`" v-for="(filter,index) in options.filters" :key="index">
          <input type="text" class="input w-full border" v-model="options.filters[filter]"
                 :style="'max-width:'+(filter=='id'?'50px':'auto')">
        </div>
        <div :slot="`h__${column}`" v-for="(column,index) in columns" :key="index" v-text="column"></div>
        <div slot="beforeTable" style="text-align: right" class="mb-3">
          <v-btn
              color="primary"
              small
              elevation="2">New Administrator
          </v-btn>
        </div>

        <div slot="image" slot-scope="props" class="text-center">
          <v-avatar
              color="primary"
              size="50">
          </v-avatar>
        </div>

        <div slot="status" slot-scope="props" class="text-center">
          <v-chip
              v-if="props.row.status"
              color="green">Activo
          </v-chip>
          <v-chip
              v-else
              color="red">Inactivo
          </v-chip>
        </div>
      </v-server-table>
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
    columns: ['image', 'pk', 'name', 'last_name', 'rol__name', 'status', 'actions'],
    options: {
      // see the options API
      filters: {
        'pk': "",
        'name': "",
        'last_name': "",
        'rol__name': "",
        'status': ""
      }
    }
  }),
}
</script>