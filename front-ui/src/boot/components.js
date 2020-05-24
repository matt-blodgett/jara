import Loading from '../components/Loading'

export default ({ app, router, Vue }) => {
  console.debug('%c initializing components', 'background-color:yellow;color:blue;font-weight:bolder')
  Vue.component('loading', Loading)
}
