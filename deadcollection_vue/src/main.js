import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://8000-sjecollins-deadcollecti-hqlw5hgkfnf.ws-eu82.gitpod.io/'

createApp(App).use(store).use(router, axios).mount('#app')
