import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/home/home.vue'
import { APP_ROUTE_NAMES } from '@/constants/routeNames'
// import ClientForm from '@/components/ClientForm.vue'
import PetForm from '@/views/pets/components/PetForm.vue'
import IndexClient from '@/views/Clients/IndexClient.vue'
import FormClient from '@/views/Clients/components/FormClient.vue'
import indexViewPets from '@/views/pets/indexViewPets.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
{ path: '/', name: APP_ROUTE_NAMES.HOME, component: Home },
  { path: '/clients-s', name: APP_ROUTE_NAMES.CLIENTS, component: IndexClient },
  {
  path: '/form-cliente/:id?', // <-- el ? hace que sea opcional
  name: APP_ROUTE_NAMES.FORM_CLIENT,
  component: FormClient
},
  {
  path: '/form-animals/:id?', // <-- el ? hace que sea opcional
  name: APP_ROUTE_NAMES.FORM_CLIENT,
  component: FormClient
},
 { path: '/pets', name: APP_ROUTE_NAMES.PETS, component: indexViewPets },
 { path: '/form-pets', name: APP_ROUTE_NAMES. FORM_PETS, component: PetForm },
  ],
})
// DEBUG: muestra en consola las rutas registradas (borra luego esto)
console.log('ROUTER REGISTERED ROUTES:', router.getRoutes().map(r => ({ name: r.name, path: r.path })))
window.__router = router // te da acceso desde consola del navegador para inspeccionar si lo necesitas

export default router
