import { createRouter, createWebHashHistory } from 'vue-router'
import Main from './pages/Main.vue'
import LogIn from './pages/LogIn.vue'
import SignUp from './pages/SignUp.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: Main },
    { path: '/login', component: LogIn },
    { path: '/signup', component: SignUp }
  ]
})
