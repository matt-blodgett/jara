import Vue from 'vue'
import Vuex from 'vuex'
import vuexCache from 'vuex-cache'
import createLogger from 'vuex/dist/logger'
import createPersistedState from 'vuex-persistedstate'
import state from './state'
import actions from './actions'
import mutations from './mutations'
import auth from './modules/auth'

Vue.use(Vuex)

const store = new Vuex.Store({
  plugins: [
    createLogger(),
    createPersistedState(),
    vuexCache
  ],
  actions,
  mutations,
  state,
  strict: (process.env.NODE_ENV !== 'production'),
  modules: {
    auth
  }
})

if (module.hot) {
  module.hot.accept([
    './actions',
    './getters',
    './mutations'
  ], () => {
    store.hotUpdate({
      actions: require('./actions'),
      getters: require('./getters'),
      mutations: require('./mutations')
    })
  })
}

export default store
