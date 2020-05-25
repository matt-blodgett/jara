const routes = [
  {
    path: '/',
    redirect: to => {
      return '/home'
    }
  },
  {
    path: '/home',
    component: () => import('layouts/TopLayout.vue'),
    children: [
      { path: '', props: true, component: () => import('pages/Home.vue'), meta: { title: route => 'Home' } }
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
