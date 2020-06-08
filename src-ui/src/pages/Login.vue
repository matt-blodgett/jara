<template>
  <q-page>
    <q-card flat class="center">
      <q-form ref="formLogin">
        <q-card-section>
          <div class="q-gutter-sm">
            <q-space class="q-pt-xs" />
            <q-input
              outlined
              label="User ID"
              v-model="form.user_id"
              :rules="[
                value => (value && value.length > 0) || 'Please enter your User ID'
              ]"
            />
            <q-space class="q-pt-xs" />
            <q-input
              outlined
              label="Password"
              v-model="form.password"
              :type="hidePassword ? 'password' : 'text'"
              @keyup.enter="submit()"
              :rules="[
                value => (value && value.length > 0) || 'Please enter your password'
              ]"
            >
              <template v-slot:append>
                <q-icon
                  class="cursor-pointer"
                  :name="hidePassword ? 'mdi-eye' : 'mdi-eye-off'"
                  @click="hidePassword = !hidePassword"
                />
              </template>
            </q-input>
          </div>
        </q-card-section>
        <q-card-actions class="q-px-md">
          <q-btn
            class="full-width q-pa-xs"
            color="primary"
            @click="submit()"
            label="Login"
          />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-page>
</template>

<script>
import { AUTH_REQUEST } from '../store/actions/auth'

export default {
  name: 'Login',
  data: function () {
    return {
      hidePassword: true,
      form: {
        user_id: null,
        password: null
      }
    }
  },
  methods: {
    submit: function () {
      this.$refs.formLogin.validate()
        .then(success => {
          if (success) {
            this.$q.loading.show({
              message: 'Logging in'
            })
            this.$store.dispatch(AUTH_REQUEST, {...this.form})
              .then(() => {
                const redirect = this.$route.query.redirect
                this.$q.loading.hide()
                this.$router.push(redirect || '/home')
              })
              .catch(() => {
                this.$q.loading.hide()
                this.$q.notify({
                  message: 'Login Failed',
                  icon: 'mdi-alert-circle',
                  color: 'negative'
                })
              })
          }
        })
    }
  }
}
</script>

<style scoped lang="stylus">
.center
  margin-left auto
  margin-right auto
.q-card
  width 20em
</style>
