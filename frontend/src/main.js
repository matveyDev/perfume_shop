import { createApp } from 'vue'
import App from './App'
import router from '../router/router.js'
import components from '../components/UI'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'


const app = createApp(App)


components.forEach(component => {
    app.component(component.name, component)
});
app.
    use(router).
    mount('#app')
