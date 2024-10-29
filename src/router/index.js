import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import SearchView from '@/views/SearchView.vue'
import LoginView from '@/views/LoginView.vue'
import DashboardView from '@/views/DashboardView.vue'
import AddGenericeView from '@/views/AddGenericeView.vue'
import AddManufacturerView from '@/views/AddManufacturerView.vue'
import AddMedicineView from '@/views/AddMedicineView.vue'
import MedicineListView from '@/views/MedicineListView.vue'
import EditMedicineView from '@/views/EditMedicineView.vue'
import AdminSearchView from '@/views/AdminSearchView.vue'
import GenericeListView from '@/views/GenericeListView.vue'
import ManufacturerListView from '@/views/ManufacturerListView.vue'

import { AuthStore } from '@/stores/auth'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/admin/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/admin/generic-list',
      name: 'generic-list',
      component: GenericeListView
    },
    {
      path: '/admin/add-generic',
      name: 'add-generic',
      component: AddGenericeView
    },
    {
      path: '/admin/add-manufacturer',
      name: 'add-manufacturer',
      component: AddManufacturerView
    },
    {
      path: '/admin/manufacturer-list',
      name: 'manufacturer-list',
      component: ManufacturerListView
    },
    {
      path: '/admin/medicine-list',
      name: 'medicine-list',
      component: MedicineListView
    },
    {
      path: '/admin/add-medicine',
      name: 'add-medicine',
      component: AddMedicineView
    },
    {
      path: '/admin/search',
      name: 'admin-search',
      component: AdminSearchView
    },
    {
      path: '/admin/update-medicine/:id',
      name: 'update-medicine',
      component: EditMedicineView
    },
  ]
})


const authenticatedRoutes = [
  'dashboard',
  'generic-list',
  'add-generic',
  'manufacturer-list',
  'add-manufacturer',
  'medicine-list',
  'add-medicine',
  'update-medicine',
  'admin-search'
 ]

router.beforeEach((to, from, next) => {
  const store = AuthStore()
  const isAuthenticated = store.isAuthenticated
  console.log(isAuthenticated)
  if (authenticatedRoutes.includes(to.name) && !isAuthenticated) next({ name: 'login' })
  else next()
})

export default router
