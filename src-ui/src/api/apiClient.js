import axios from 'axios'

import useDevLogging from './interceptors/dev-logging'
import useError from './interceptors/api-error'

const apiClient = axios.create({
  baseURL: '/api'
})

if (process.env.NODE_ENV !== 'production') {
  useDevLogging(apiClient)
}

useError(apiClient)

export { apiClient }
