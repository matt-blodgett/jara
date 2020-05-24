/**
 * Set Global Config for Vue here
 * https://vuejs.org/v2/api/#Global-Config
 */

export default ({ Vue }) => {
  Object.assign(Vue.config, {
    performance: process.env.NODE_ENV !== 'production'
  })
}
