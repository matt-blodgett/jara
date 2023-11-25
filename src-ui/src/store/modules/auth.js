import { apiClient } from '@/api'
import {
  AUTH_REQUEST,
  AUTH_SUCCESS,
  AUTH_ERROR,
  AUTH_CLEAR
} from '@/store/types/auth'

const state = {
  profile: {},
  token: null
}

const getters = {
  userProfile: state => state.profile,
  isAuthenticated: state => !!state.token
}

const mutations = {
  [AUTH_SUCCESS]: (state, response) => {
    state.profile = response.profile
    state.token = response.token
    apiClient.defaults.headers.common['Authorization'] = `Token ${state.token}`
  },
  [AUTH_ERROR]: (state) => {
    state.profile = {}
    state.token = null
  },
  [AUTH_CLEAR]: (state) => {
    state.profile = {}
    state.token = null
    delete apiClient.defaults.headers.common['Authorization']
  }
}

const actions = {
  [AUTH_REQUEST]: ({ commit, dispatch }, data) => {
    return new Promise((resolve, reject) => {
      commit(AUTH_CLEAR)
      apiClient.post('/users/auth', data).then(response => {
        if (response.status === 200) {
          commit(AUTH_SUCCESS, response.data)
          resolve(response.data)
        } else {
          commit(AUTH_ERROR)
          reject(response.data)
        }
      }).catch(error => {
        commit(AUTH_ERROR)
        reject(error)
      })
    })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
