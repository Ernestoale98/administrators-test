<template>
  <v-container>
    <v-breadcrumbs
        :items="breadcrumbs">
      <template v-slot:divider>
        <v-icon>arrow_forward</v-icon>
      </template>
      <template v-slot:item="{ item }">
        <v-breadcrumbs-item>
          <router-link :to="item.href" v-text="item.text"></router-link>
        </v-breadcrumbs-item>
      </template>
    </v-breadcrumbs>
    <div id="people">
      <v-server-table ref="table" url="administrators" :columns="columns" :options="options">
        <div :slot="`filter__${filter}`" v-for="(filter,index) in options.filters" :key="index">
          <input type="text" class="input w-full border" v-model="options.filters[filter]"
                 :style="'max-width:'+(filter=='id'?'50px':'auto')">
        </div>
        <div :slot="`h__${column.name}`" v-for="(column,index) in options.columns" :key="index"
             v-text="column.text"></div>
        <div slot="beforeTable" style="text-align: right" class="mb-3">
          <v-btn
              @click="openModal()"
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
              label
              color="success">Activo
          </v-chip>
          <v-chip
              v-else
              label
              text-color="white"
              color="red">Inactivo
          </v-chip>
        </div>

        <div slot="actions" slot-scope="props" class="text-center">
          <v-btn
              @click="edit(props.row.pk)"
              icon
              color="blue">
            <v-icon>edit</v-icon>
          </v-btn>
          <v-btn
              @click="show(props.row.pk)"
              icon
              color="gray">
            <v-icon>remove_red_eye</v-icon>
          </v-btn>
          <v-btn
              @click="erase(props.row.pk)"
              icon
              color="red">
            <v-icon>restore_from_trash</v-icon>
          </v-btn>
        </div>
      </v-server-table>
    </div>
    <administrator-modal @created="$refs.table.refresh()"></administrator-modal>
  </v-container>
</template>

<script>
import AdministratorModal from "./AdministratorModal";
import Swal from 'sweetalert2'

export default {
  name: "AdministratorsTable",
  components: {
    AdministratorModal,
    Swal
  },
  data: () => ({
    breadcrumbs: [
      {
        text: 'Inicio',
        disabled: false,
        href: 'dashboard',
      },
      {
        text: 'Administradores',
        disabled: false,
        href: 'administrators',
      }
    ],
    columns: ['pk', 'user__first_name', 'user__last_name', 'user__email', 'rol__name', 'status', 'actions'],
    options: {
      // see the options API
      columns: [
        {
          'name': 'pk',
          'text': 'Id'
        },
        {
          'name': 'user__first_name',
          'text': 'Name'
        },
        {
          'name': 'user__last_name',
          'text': 'Last Name'
        },
        {
          'name': 'user__email',
          'text': 'Email'
        },
        {
          'name': 'rol__name',
          'text': 'Rol'
        },
        {
          'name': 'status',
          'text': 'Status'
        },
        {
          'name': 'actions',
          'text': 'Actions'
        }
      ],
      filters: {
        'pk': "",
        'name': "",
        'last_name': "",
        'rol__name': "",
        'status': ""
      }
    },
    dialog: false
  }),
  methods: {
    openModal() {
      this.$modal.show('administrator-modal')
    },
    edit(id) {
      this.$modal.show('administrator-modal', {
        id: id,
        'action': 'update'
      })
    },
    show(id) {
      this.$modal.show('administrator-modal', {
        id: id,
        'action': 'show'
      })
    },
    erase(id) {
      Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          axios.delete(`administrators/${id}/delete/`).then(response => {
            this.$refs.table.refresh()
            Swal.fire(
                'Deleted!',
                'Administrator has been deleted',
                'success'
            )
          }).catch(error => {

          });

        }
      })
    }
  }
}
</script>