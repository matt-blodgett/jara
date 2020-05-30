const routes = [
  {
    path: '/',
    redirect: to => {
      return '/login'
    }
  },
  {
    path: '/login',
    component: () => import('layouts/TopLayoutLogin.vue'),
    children: [
      { path: '', props: true, component: () => import('pages/Login.vue'), meta: { title: route => 'Login' } }
    ]
  },
  {
    path: '/pages',
    component: () => import('layouts/TopLayout.vue'),
    children: [
      { path: 'home', props: true, component: () => import('pages/Home.vue'), meta: { title: route => 'Home' } }
    ]
  },
  {
    path: '/401-unauthorized',
    component: () => import('layouts/TopLayout.vue'),
    children: [
      { path: '', props: true, component: () => import('pages/Error401.vue'), meta: { title: route => '401 Unauthorized' } }
    ]
  },
  {
    path: '*',
    component: () => import('layouts/TopLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Error404.vue'), meta: { title: route => '404 Not Found' } }
    ]
  }
]

export default routes
