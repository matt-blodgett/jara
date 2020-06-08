<template>
  <q-layout view="hhh lpr fff">

    <q-header elevated style="bg-black">
      <q-toolbar>
        <q-btn flat round dense icon="mdi-menu" @click="drawer.left = !drawer.left" />
        <q-toolbar-title>Header</q-toolbar-title>
        <q-btn flat round dense icon="mdi-menu" @click="drawer.right = !drawer.right" />
      </q-toolbar>
    </q-header>

    <q-drawer
      side="left"
      elevated
      bordered
      show-if-above
      :width="200"
      :breakpoint="500"
      content-class="bg-grey-3"
      v-model="drawer.left"
    >
      <q-scroll-area class="fit">
      </q-scroll-area>
    </q-drawer>

    <q-drawer
      side="right"
      elevated
      bordered
      show-if-above
      :width="200"
      :breakpoint="500"
      content-class="bg-grey-3"
      v-model="drawer.right"
    >
      <q-scroll-area class="fit">
        <q-list separator padding>

          <q-item v-if="!isAuthenticated" v-ripple clickable @click="signIn()">
            <q-item-section avatar>
              <q-icon name="mdi-account" />
            </q-item-section>
            <q-item-section>Sign In</q-item-section>
          </q-item>

          <q-item v-if="isAuthenticated" v-ripple clickable @click="signOut()">
            <q-item-section avatar>
              <q-icon name="mdi-account" />
            </q-item-section>
            <q-item-section>Sign Out</q-item-section>
          </q-item>

        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>
    </q-footer>

  </q-layout>
</template>

<script>
import { AUTH_LOGOUT } from 'src/store/actions/auth'

export default {
  name: 'TopLayout',
  data: function () {
    return {
      drawer: {
        left: false,
        right: false
      }
    }
  },
  computed: {
    isAuthenticated: function () {
      return this.$store.getters.isAuthenticated
    }
  },
  methods: {
    signIn: function () {
      this.$router.push({ path: '/login' })
    },
    signOut: function () {
      this.$store.dispatch(AUTH_LOGOUT)
      this.$q.notify({
        color: 'negative',
        icon: 'mdi-alert',
        message: 'Logged out.'
      })
    }
  }
}
</script>

<style scoped lang="stylus">
</style>
