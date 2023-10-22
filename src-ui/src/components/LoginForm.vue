<template>
  <v-sheet :border="true" class="pa-6 mx-auto" rounded :width="500">

    <h2 class="text-h5 mb-6">Login</h2>

    <v-alert
      class="my-6"
      closable
      color="error"
      icon="$error"
      title="Login Failed"
      text="Invalid username or password"
      v-model="isErrorSubmit"
    />

    <v-form ref="form" fast-fail>
      <v-text-field
        label="Username"
        required
        :counter="30"
        v-model="formData.username"
      />
      <v-text-field
        label="Password"
        required
        v-model="formData.password"
      />

      <div class="text-right">
        <a href="/reset-password">Forgot password?</a>
      </div>

      <v-divider class="my-4" />

      <div class="text-center mt-6">
        <v-btn color="primary" text="Login" @click="submit()" :loading="isLoadingSubmit" />
      </div>
    </v-form>

    <div class="text-center mt-12">
      <div>Not registered? <a href="/sign-up">Create an account</a></div>
    </div>

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
        username: null,
        password: null
      }
    }
  },
  methods: {
    async submit () {
      const { valid } = await this.$refs.form.validate()
      if (valid) {
        this.isErrorSubmit = false
        this.isLoadingSubmit = true
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
      }
    }
  }
}
</script>
