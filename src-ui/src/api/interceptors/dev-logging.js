function getUrl (config) {
  if (config.baseURL) {
    return config.url.replace(config.baseURL, '')
  }
  return config.url
}

export default axios => {
  axios.interceptors.request.use(
    (config) => {
      console.log('%c ' + config.method.toUpperCase() + ' - ' + getUrl(config) + ':', 'color: #0086b3; font-weight: bold', config)
      return config
    },
    (error) => {
      return Promise.reject(error)
    }
  )

  axios.interceptors.response.use(
    (response) => {
      console.log('%c ' + response.status + ' - ' + getUrl(response.config) + ':', 'color: #008000; font-weight: bold', response)
      return response
    },

    (error) => {
      const status = error.response ? error.response.status : 'No response'
      console.log('%c ' + status + ' - ' + ':', 'color: #a71d5d; font-weight: bold', error)
      return Promise.reject(error)
    }
  )
}
