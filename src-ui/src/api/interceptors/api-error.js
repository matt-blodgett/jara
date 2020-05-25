export default axios => {
  axios.interceptors.response.use(
    (response) => {
      return response
    },
    (error) => {
      const response = error.response
      if (response) {
        console.log('%c ' + 'HTTP' + response.status + ' - ' + ':', 'color: #a71d5d; font-weight: bold', error)
      }
      return Promise.reject(error)
    })
}
