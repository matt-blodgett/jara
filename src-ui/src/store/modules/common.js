import {
  NOTIFY_SHOW,
  NOTIFY_HIDE
} from '@/store/types/common'

const state = {
  notify: {
    type: null,
    message: null,
    timeout: null,
    visible: false
  }
}

const getters = {
  notify: state => state.notify
}

const mutations = {
  [NOTIFY_SHOW]: (state, data) => {
    state.notify.visible = false
    state.notify.type = data.type
    state.notify.message = data.message
    state.notify.timeout = data?.timeout || 2_000
    state.notify.visible = true
  },
  [NOTIFY_HIDE]: (state) => {
    state.notify = {
      type: null,
      message: null,
      timeout: null,
      visible: false
    }
  }
}

export default {
  state,
  getters,
  mutations
}
