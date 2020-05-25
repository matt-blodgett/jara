/**
 * root Vuex actions
 */
const actions = {
  initialiseStore (state) {
    console.debug('%c actions.initialiseStore ', 'color:navy;background-color:yellow')
    let savedState = localStorage.getItem('jara-store')
    if (savedState) {
      this.replaceState(Object.assign(state, JSON.parse(savedState)))
    }
  }
}

export default actions
