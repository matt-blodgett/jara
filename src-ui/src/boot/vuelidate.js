import Vuelidate from 'vuelidate'

export default ({ Vue }) => {
  console.debug('%c initializing plugin vuelidate', 'background-color:yellow;color:blue;font-weight:bolder')
  Vue.use(Vuelidate)
}
