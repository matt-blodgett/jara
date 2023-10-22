import axios from 'axios'

import useDevLogging from './interceptors/dev-logging'

const apiClient = axios.create({
  baseURL: '/api'
})

if (process.env.NODE_ENV !== 'production') {
  useDevLogging(apiClient)
}

export { apiClient }
