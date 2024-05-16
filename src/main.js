import { createApp } from 'vue'
import { createPinia } from 'pinia'

// 부트스트랩
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
// Vuetify
import vuetify from './plugins/vuetify';

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

pinia.use(piniaPluginPersistedstate)
app.use(createPinia())
app.use(router)
app.use(BootstrapVue3)
app.use(vuetify)

app.mount('#app')
