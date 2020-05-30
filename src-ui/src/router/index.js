import Vue from 'vue'
import VueRouter from 'vue-router'
import { LoadingBar } from 'quasar'
import routes from './routes'

Vue.use(VueRouter)

const ROOT_PAGE_TITLE = 'Jara'

LoadingBar.setDefaults({
  color: 'red',
  size: '2px',
  position: 'top'
})

function callOrPassThrough (maybeFunction, ...args) {
  return typeof maybeFunction === 'function' ? maybeFunction(...args) : maybeFunction
}

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ y: 0 }),
    routes,
    // Leave these as is and change from quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  {
    let currentState = false
    const toggleLoadingBar = state => {
      if (state === currentState) return
      LoadingBar[state ? 'start' : 'stop']()
      currentState = state
    }
    Router.beforeEach((to, from, next) => {
      toggleLoadingBar(true)
      next()
    })
    Router.afterEach((to, from) => {
      toggleLoadingBar(false)
    })
  }

  Router.afterEach((to, from) => {
    Vue.nextTick(() => {
      const routePageTitlePart = callOrPassThrough(to.meta.title, to)
      window.document.title = routePageTitlePart ? `${ROOT_PAGE_TITLE} / ${routePageTitlePart}` : ROOT_PAGE_TITLE
    })
  })

  return Router
}
