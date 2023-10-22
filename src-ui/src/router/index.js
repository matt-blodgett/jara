import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

const routes = [
  {
    path: '/login',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        component: () => import('@/views/Login.vue'),
        meta: {
          title: 'Login'
        }
      }
    ]
  },
  {
    path: '/',
    component: () => import('@/layouts/Main.vue'),
    children: [
      {
        path: '',
        redirect: to => {
          const isAuthenticated = store.getters.isAuthenticated
          if (isAuthenticated) {
            return { path: '/home' }
          }
          return { path: '/login' }
        }
      },
      {
        path: 'home',
        component: () => import('@/views/Home.vue'),
        meta: {
          title: 'Home'
        }
      },
      {
        path: 'test',
        component: () => import('@/views/Test.vue'),
        meta: {
          title: 'Test'
        }
      },
      {
        path: '401-unauthorized',
        component: () => import('@/views/Error401.vue'),
        meta: {
          title: '401 Unauthorized'
        }
      }
    ]
  },
  {
    path: '/:unknownPath(.*)',
    component: () => import('@/layouts/Default.vue'),
    children: [
      { 
        path: '',
        component: () => import('@/views/Error404.vue'),
        meta: {
          title: '404 Not Found'
        }
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.onError((error, to) => {
  // "Importing a module script failed"
  if (error.message.includes('Failed to fetch dynamically imported module')) {
    window.location.href = to.fullPath
  }
})

router.afterEach((to, from) => {
  const titleDefault = 'Jara'
  const titleRoute = to.meta.title
  const titleWindow = titleRoute || titleDefault
  window.document.title = titleWindow
})

export default router
