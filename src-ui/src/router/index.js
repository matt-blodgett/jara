import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

const routes = [
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
        path: 'login',
        component: () => import('@/views/Login.vue'),
        meta: {
          title: 'Login'
        }
      },
      {
        path: 'reset-password',
        component: () => import('@/views/ResetPassword.vue'),
        meta: {
          title: 'Reset Password'
        }
      },
      {
        path: 'sign-up',
        component: () => import('@/views/SignUp.vue'),
        meta: {
          title: 'Sign Up'
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
        path: 'profile',
        component: () => import('@/views/Profile.vue'),
        meta: {
          title: 'Profile'
        }
      },
      {
        path: 'settings',
        component: () => import('@/views/Settings.vue'),
        meta: {
          title: 'Settings'
        }
      },
      {
        path: 'recipes',
        component: () => import('@/views/Recipes.vue'),
        meta: {
          title: 'Recipes'
        }
      },
      {
        path: 'about',
        component: () => import('@/views/About.vue'),
        meta: {
          title: 'About'
        }
      },
      {
        path: 'error-401',
        component: () => import('@/views/Error401.vue'),
        meta: {
          title: '401 Unauthorized'
        }
      },
      { 
        path: 'error-404',
        component: () => import('@/views/Error404.vue'),
        meta: {
          title: '404 Not Found'
        }
      }
    ]
  },
  {
    path: '/:unknownPath(.*)',
    redirect: to => {
      return { path: '/error-404' }
    }
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
