import { apiClient } from 'src/api'

export default ({ Vue }) => {
  Vue.prototype.$apiClient = apiClient
}
