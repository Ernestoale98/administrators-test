<template>
  <modal name="administrator-modal" height="auto" width="800px" @before-open="beforeOpen">
    <v-container>
      <div class="modal-header">
        New Administrator
      </div>
      <hr>
      <br>
      <v-row>
        <v-col cols="12">
          <v-form v-model="validateForm">
            <v-text-field
                label="Name"
                :rules="[rules.required, rules.min]"
                outlined
                v-model="administrator.name"></v-text-field>
            <v-text-field
                label="Last Name"
                :rules="[rules.required, rules.min]"
                outlined
                v-model="administrator.last_name"></v-text-field>
            <v-text-field
                label="Email"
                :rules="[rules.required, rules.email]"
                outlined
                v-model="administrator.email"></v-text-field>
            <v-select
                :items="roles"
                :rules="[rules.required]"
                label="Rol"
                v-model="administrator.rol"
                outlined></v-select>
            <v-select
                :rules="[rules.required]"
                :items="status"
                v-model="administrator.status"
                label="Status"
                outlined
            ></v-select>
            <v-text-field
                v-model="administrator.password"
                :rules="[rules.required, rules.min]"
                :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPass ? 'text' : 'password'"
                label="Password"
                hint="At least 8 characters"
                counter
                outlined
                @click:append="showPass = !showPass"
            ></v-text-field>
            <hr>
            <br>
            <div style="text-align: right" class="mb-3">
              <v-btn
                  @click="save()"
                  style="text-align: right"
                  class="ma-2 text-right"
                  :loading="loading"
                  :disabled="loading || !validateForm"
                  color="success">Save
              </v-btn>
            </div>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </modal>
</template>

<script>
export default {
  name: "CollaboratorModal",
  data() {
    return {
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        },
      },
      administrator: {
        name: '',
        last_name: '',
        rol: '',
        status: true,
        password: ''
      },
      status: [{
        'text': 'Activo',
        'value': true
      }, {
        'text': 'Inactivo',
        'value': false
      }],
      roles: [],
      loading: false,
      showPass: false,
      validateForm: false
    }
  },
  methods: {
    beforeOpen(event) {
      this.getRoles();
    },
    getRoles() {
      axios.get('/roles').then(response => {
        this.roles = response.data['data'].map(rol => {
          return {
            'text': rol.name,
            'value': rol.pk
          }
        })
      }).catch(error => {

      })
    },
    save() {
      this.loading = true;
      axios.post('/administrators/store/', this.administrator).then(response => {
        this.$toastr.s('Administrator created');
        this.$modal.hide('administrator-modal');
        this.$emit('created');
      }).catch(error => {

      });
    }
  }
}
</script>