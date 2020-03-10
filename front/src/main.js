import Vue from 'vue'
import VeeValidate , { Validator } from 'vee-validate';
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import {store} from './store';

import ru from 'vee-validate/dist/locale/ru'

Vue.use(BootstrapVue)

Vue.config.productionTip = false
Vue.use(VeeValidate);
Validator.localize('ru', ru);
new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
