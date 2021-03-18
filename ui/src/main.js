import Vue from 'vue'
import App from './App.vue'

//Components
import HelloWord from './components/HelloWorld.vue'

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    components: {
        HelloWord
    }
}).$mount('#app')
