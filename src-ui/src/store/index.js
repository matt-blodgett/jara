import { createStore } from 'vuex'
import VuexPersistence from 'vuex-persist'
import common from './modules/common'
import auth from './modules/auth'

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

const store = createStore({
  plugins: [
    vuexLocal.plugin
  ],
  strict: (process.env.NODE_ENV !== 'production'),
  modules: {
    common,
    auth
  }
})

export default store
