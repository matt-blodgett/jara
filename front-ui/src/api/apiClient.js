import axios from 'axios'

import useApiValidation from './interceptors/api-validation'
import useDevLogging from './interceptors/dev-logging'
import useError from './interceptors/api-error'

const apiClient = axios.create({
  baseURL: '/api'
})

if (process.env.NODE_ENV !== 'production') {
  useDevLogging(apiClient)
}

useApiValidation(apiClient)
useError(apiClient)

export { apiClient }
