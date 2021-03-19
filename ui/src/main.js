import VtTable from "./components/vue-table/VtTable";

require('./bootsrap');
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Vue from 'vue'
import App from './App.vue'

import vuetify from './plugins/vuetify';

import VueRouter from "vue-router";

import {ServerTable} from 'vue-tables-2'

import VModal from 'vue-js-modal';

//Components
import AdministratorsTable from "./components/adminitrators/AdministratorsTable";
//VueTableComponents
import VtGenericFilter from "./components/vue-table/VtGenericFilter";
import VtDataTable from "./components/vue-table/VtDataTable";
import VtSortControl from "./components/vue-table/VtSortControl";
import VtPagination from "./components/vue-table/VtPagination";
import VtPerPageSelector from "./components/vue-table/VtPerPageSelector";

Vue.use(VueRouter)
Vue.use(ServerTable, {}, false, 'bootstrap4', {
    table: VtTable,
    genericFilter: VtGenericFilter,
    dataTable: VtDataTable,
    sortControl: VtSortControl,
    pagination: VtPagination,
    perPageSelector: VtPerPageSelector
});
Vue.use(VModal)

Vue.config.productionTip = false

const routes = [
    {path: '/administrators', component: AdministratorsTable}
]

const router = new VueRouter({
    routes
})

new Vue({
    render: h => h(App),
    vuetify,
    router
}).$mount('#app')
