import axios from 'axios'

export default ({ Vue }) => {
  console.debug('%c initializing plugin axios', 'background-color:yellow;color:blue;font-weight:bolder')
  Vue.prototype.$axios = axios
}
