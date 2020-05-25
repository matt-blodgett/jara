import APIs from '../apis/index'
import memoize from 'lodash/memoize'
import pathtoRegexp from 'path-to-regexp'

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

function doesPathMatch (config, api) {
  return memoizedPathtoRegexp(api.pattern)
    .test(removeQueryString(config.url))
}

function mapRequestConfigToApi (config) {
  return APIs.find(api => doesMethodMatch(config, api) && doesPathMatch(config, api))
}

export default axios => {
  axios.interceptors.request.use(config => {
    const api = mapRequestConfigToApi(config)
    if (!api) {
      throw new Error(`No defined API matching '${config.method.toUpperCase()} ${config.url}'`)
    }
    return config
  })
}
