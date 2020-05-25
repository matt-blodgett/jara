import APIs from '../apis/index'
import memoize from 'lodash/memoize'
import pathtoRegexp from 'path-to-regexp'
import { Notify } from 'quasar'

const memoizedPathtoRegexp = memoize(pathtoRegexp)
const removeQueryString = url => url.split('?')[0]

function doesMethodMatch (config, api) {
  if (Array.isArray(api.method)) {
    return api.method
      .map(method => method.toLowerCase())
      .includes(config.method.toLowerCase())
  } else {
    return config.method.toLowerCase() === api.method.toLowerCase()
  }
}

function doesResponsePathMatch (config, api) {
  return memoizedPathtoRegexp('/api/' + api.pattern)
    .test(removeQueryString(config.url))
}

function mapErrorConfigToApi (config) {
  return APIs.find(api => doesMethodMatch(config, api) && doesResponsePathMatch(config, api))
}

export default axios => {
  axios.interceptors.response.use(
    (response) => {
      return response
    },
    (error) => {
      const response = error.response
      if (response) {
        const api = mapErrorConfigToApi(response.config)
        if (api && !api.disableError) {
          if (response.status === 404) {
            var msg = 'Not found'
            if (response.data) {
              msg = JSON.stringify(response.data)
            }
            Notify.create({
              icon: 'error',
              color: 'negative',
              message: msg
            })
          }
        }
      }
      return Promise.reject(error)
    })
}
