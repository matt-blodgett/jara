<template>
  <v-sheet :border="true" class="pa-6 mx-auto" rounded :width="500">

    <h2 class="text-h5 mb-6">Sign Up</h2>

    <v-alert
      class="my-6"
      closable
      color="error"
      icon="$error"
      title="Registration Failed"
      text="There was an error creating your account"
      v-model="isErrorSubmit"
    />

    <v-form ref="form" fast-fail @submit.prevent="submit">

      <v-text-field
        label="Email"
        v-model="formData.email"
        :rules="formRules.email"
        :error-messages="formErrorMessages.email"
        :maxlength="128"
        counter
        density="compact"
        variant="outlined"
        prepend-inner-icon="mdi-email-outline"
      />

      <v-text-field
        label="Username"
        v-model="formData.username"
        :rules="formRules.username"
        :error-messages="formErrorMessages.username"
        :maxlength="30"
        counter
        density="compact"
        variant="outlined"
        prepend-inner-icon="mdi-account"
      />

      <v-text-field
        label="Password"
        v-model="formData.password"
        :type="formTypes.password"
        :rules="formRules.password"
        :maxlength="128"
        density="compact"
        variant="outlined"
        prepend-inner-icon="mdi-lock-outline"
        :append-inner-icon="formTypes.password === 'password' ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append-inner="formTypes.password = formTypes.password === 'password' ? 'text' : 'password'"
        autocomplete="on"
      />

      <v-text-field
        label="Confirm Password"
        v-model="formData.confirmPassword"
        :type="formTypes.confirmPassword"
        :rules="formRules.confirmPassword"
        :maxlength="128"
        density="compact"
        variant="outlined"
        prepend-inner-icon="mdi-lock-outline"
        :append-inner-icon="formTypes.confirmPassword === 'password' ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append-inner="formTypes.confirmPassword = formTypes.confirmPassword === 'password' ? 'text' : 'password'"
        autocomplete="on"
      />

      <v-divider class="mb-4" />

      <div class="text-center">
        <v-btn color="primary" text="Submit" @click="submit()" :loading="isLoadingSubmit" />
      </div>

    </v-form>

  </v-sheet>
</template>

<script>
import { AUTH_REQUEST } from '@/store/types/auth'
import { NOTIFY_SHOW } from '@/store/types/common'

export default {
  data () {
    return {
      isLoadingSubmit: false,
      isErrorSubmit: false,
      formData: {
        email: null,
        username: null,
        password: null,
        confirmPassword: null
      },
      formRules: {
        email: [
          value => {
            if (!value) {
              return 'Field is required'
            } else if (value.length > 128) {
              return 'Email must be less than 128 characters long'
            } else if (!value.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
              return 'Invalid email'
            } else {
              this.checkEmailExists(value)
            }
            return true
          }
        ],
        username: [
          value => {
            if (!value) {
              return 'Field is required'
            } else if (value.length < 3) {
              return 'Username must be at least 3 characters long'
            } else if (value.length > 30) {
              return 'Username must be less than 30 characters long'
            } else {
              this.checkUsernameExists(value)
            }
            return true
          }
        ],
        password: [
          value => {
            if (!value) {
              return 'Field is required'
            } else if (value.length < 8) {
              return 'Password must be at least 8 characters long'
            } else if (!value.match(/[A-Z]/)) {
              return 'Password must include at least one upper case letter'
            } else if (!value.match(/[a-z]/)) {
              return 'Password must include at least one lower case letter'
            } else if (!value.match(/[0-9]/)) {
              return 'Password must include at least one number 0-9'
            } else if (!value.match(/!|%|\^|\*|\(|\)|_|-|\+|=|<|>|\||\\|\[|\]/)) {
              return 'Password must include at least one special character ! % ^ * ( ) _ - + = < > | \ [ ]'
            }
            return true
          }
        ],
        confirmPassword: [
          value => {
            if (value !== this.formData.password) {
              return 'Passwords must match'
            }
            return true
          }
        ]
      },
      formErrorMessages: {
        username: null,
        email: null
      },
      formTypes: {
        password: 'password',
        confirmPassword: 'password'
      }
    }
  },
  methods: {
    checkUsernameExists (username) {
      const url = '/users/check_exists'
      const params = {
        type: 'username',
        value: username
      }
      this.$apiClient.get(url, { params: params }).then(response => {
        this.formErrorMessages.username = response.data.exists ? 'That username is already taken' : null
      })
    },
    checkEmailExists (email) {
      const url = '/users/check_exists'
      const params = {
        type: 'email',
        value: email
      }
      this.$apiClient.get(url, { params: params }).then(response => {
        this.formErrorMessages.email = response.data.exists ? 'An account with that email address already exists' : null
      })
    },
    async submit () {
      const { valid } = await this.$refs.form.validate()
      if (valid) {
        const url = '/users/users'
        this.isErrorSubmit = false
        this.isLoadingSubmit = true
        this.$apiClient.post(url, this.formData).then(response => {
          this.$store.commit(NOTIFY_SHOW, {
            type: 'success',
            message: 'Registration successful'
          })
          this.$store.dispatch(AUTH_REQUEST, this.formData).then(response => {
            this.isLoadingSubmit = false
            this.$store.commit(NOTIFY_SHOW, {
              type: 'success',
              message: 'Login successful'
            })
            this.$router.push({ path: '/home' })
          }).catch(error => {
            this.isErrorSubmit = true
            this.isLoadingSubmit = false
            this.$store.commit(NOTIFY_SHOW, {
              type: 'error',
              message: 'Login failed'
            })
          })
        }).catch(error => {
          this.isErrorSubmit = true
          this.isLoadingSubmit = false
          this.$store.commit(NOTIFY_SHOW, {
            type: 'error',
            message: 'Registration failed'
          })
        })
      }
    }
  }
}
</script>
