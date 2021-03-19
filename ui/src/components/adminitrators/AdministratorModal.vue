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
                :disabled="onlyShow"
                label="Name"
                :rules="[rules.required, rules.min]"
                outlined
                v-model="administrator.name"></v-text-field>
            <v-text-field
                :disabled="onlyShow"
                label="Last Name"
                :rules="[rules.required, rules.min]"
                outlined
                v-model="administrator.last_name"></v-text-field>
            <v-text-field
                :disabled="onlyShow"
                label="Email"
                :rules="[rules.required, rules.email]"
                outlined
                v-model="administrator.email"></v-text-field>
            <v-select
                :disabled="onlyShow"
                :items="roles"
                :rules="[rules.required]"
                label="Rol"
                v-model="administrator.rol"
                outlined></v-select>
            <v-select
                :disabled="onlyShow"
                :items="status"
                v-model="administrator.status"
                label="Status"
                outlined
            ></v-select>
            <v-text-field
                v-if="action ==='store'"
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
                  v-if="action==='store'"
                  @click="save()"
                  style="text-align: right"
                  class="ma-2 text-right"
                  :loading="loading"
                  :disabled="loading || !validateForm"
                  color="success">Save
              </v-btn>
              <v-btn
                  v-if="action==='update'"
                  @click="update()"
                  style="text-align: right"
                  class="ma-2 text-right"
                  :loading="loading"
                  :disabled="loading || !validateForm"
                  color="warning">Update
              </v-btn>
            </div>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </modal>
</template>

<script>
import Swal from 'sweetalert2'

export default {
  name: "CollaboratorModal",
  components: {
    Swal
  },
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
        email: '',
        rol: '',
        status: true,
        password: '',
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
      validateForm: false,
      action: '',
      onlyShow: false
    }
  },
  methods: {
    beforeOpen(event) {
      //Clean
      this.loading = false;
      this.showPass = false;
      this.action = '';
      this.onlyShow = false;
      this.getRoles();
      if (typeof event.params !== 'undefined') {
        this.getAdministrator(event.params.id);
        if (event.params.action === 'show') {
          this.onlyShow = true;
        } else {
          this.action = 'update';
          this.administrator.id = event.params.id;
        }
      } else {
        this.action = 'store';
        Object.assign(this.administrator, this.$options.data().administrator);
      }
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
        this.$modal.hide('administrator-modal');
        this.$emit('created');
        Swal.fire(
            'Created!',
            'Administrator has been created',
            'success'
        )
      }).catch(error => {

      });
    },
    update() {
      console.log(this.administrator)
      const id = this.administrator.id;
      this.loading = true;
      axios.put(`/administrators/${id}/update/`, this.administrator).then(response => {
        this.$modal.hide('administrator-modal');
        this.$emit('created');
        Swal.fire(
            'Updated!',
            'Administrator has been updated',
            'success'
        )
      }).catch(error => {

      });
    },
    getAdministrator(id) {
      axios.get(`/administrators/${id}`).then(response => {
        let data = response.data[0];
        data.name = data['user__first_name'];
        delete data['user__first_name'];
        data.last_name = data['user__last_name'];
        delete data['user__last_name'];
        data.email = data['user__email'];
        delete data['user__email']
        data.rol = data['rol__id'];
        delete data['rol__id']
        Object.assign(this.administrator, data);
        console.log(this.administrator)
      }).catch(error => {

      })
    }
  }
}
</script>