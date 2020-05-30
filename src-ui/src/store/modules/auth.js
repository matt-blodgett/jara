// import Vue from 'vue'
import axios from 'axios'
import { apiClient } from '../../api'
import {
  AUTH_REQUEST,
  AUTH_SUCCESS,
  AUTH_ERROR,
  AUTH_CLEAR,
  AUTH_LOGOUT
} from '../actions/auth'

const state = {
  profile: {},
  token: undefined
}

const getters = {
  userProfile: state => state.profile
}

const actions = {
  [AUTH_REQUEST]: ({ commit, dispatch }, data) => {
    console.debug('%c AUTH_REQUEST ', 'color:white;font-weight:bold')
    return new Promise((resolve, reject) => {
      commit(AUTH_CLEAR)
      apiClient.post('authenticate', data).then(response => {
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
  },
  [AUTH_LOGOUT]: ({ commit, dispatch }) => {
    return new Promise((resolve, reject) => {
      console.debug('%c AUTH_LOGOUT ', 'color:white;font-weight:bold')
      commit(AUTH_CLEAR)
      resolve()
    })
  }
}

const mutations = {
  [AUTH_SUCCESS]: (state, response) => {
    state.profile = response.profile
    state.token = response.token
    axios.defaults.headers.common.Authorization = `Token ${state.token}`
    console.debug('%c AUTH_SUCCESS ', 'color:green;font-weight:bold')
  },
  [AUTH_ERROR]: (state) => {
    state.profile = {}
    state.token = undefined
    console.debug('%c AUTH_ERROR ', 'color:red;font-weight:bold')
  },
  [AUTH_CLEAR]: (state) => {
    state.profile = {}
    state.token = undefined
    delete axios.defaults.headers.common.Authorization
    console.debug('%c AUTH_CLEAR ', 'color:white;font-weight:bold')
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
