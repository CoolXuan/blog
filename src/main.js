import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
 
const app = createApp(App)
app.component('QuillEditor', QuillEditor)
app.use(router).mount('#app')
