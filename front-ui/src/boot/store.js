import store from '../store'
import { sync } from 'vuex-router-sync'

export default ({ app, router, Vue }) => {
  /*
  * configure vuex-router-sync which stores vue-router's current $route as part of vuex store's state
  * const unsync = sync(store, router) // unsync() can be called later to unsync store from the router during app/Vue teardown to release resources
  */
  console.debug('%c initializing plugin store', 'background-color:yellow;color:blue;font-weight:bolder')
  sync(store, router)
  store.dispatch('initialiseStore')
}
