import vuetify from './vuetify'
import router from '@/router'
import store from '@/store'
import { apiClient } from '@/api'

export function registerPlugins (app) {
  app.use(vuetify)
  app.use(router)
  app.use(store)

  app.config.globalProperties.$apiClient = apiClient
}
