import { createStore } from 'vuex'
import VuexPersistence from 'vuex-persist'
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
    auth
  }
})

// add to jsconfig.json compilerOptions
//     "types": ["vite/client"],

// if (import.meta.hot) {
//   import.meta.hot.accept([
//     './modules/auth'
//   ], () => {
//     const newModuleAuth = require('./modules/auth').default
//     store.hotUpdate({
//       modules: {
//         auth: newModuleAuth
//       }
//     })
//   })
// }

export default store
