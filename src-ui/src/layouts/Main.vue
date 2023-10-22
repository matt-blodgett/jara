<template>
  <v-app>

    <v-app-bar color="primary" prominent>
      <v-app-bar-nav-icon
        v-if="$store.getters.isAuthenticated"
        variant="text"
        @click="isDrawerOpen = !isDrawerOpen"
      />
      <v-toolbar-title>Jara</v-toolbar-title>
      <div>{{ appVersion }}</div>
      <v-spacer />
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon="mdi-dots-vertical" v-bind="props" />
        </template>
        <v-list v-if="!$store.getters.isAuthenticated">
          <v-list-item prepend-icon="mdi-login" title="Sign In" @click="goToLogin()" />
        </v-list>
        <v-list v-if="$store.getters.isAuthenticated">
          <v-list-item prepend-icon="mdi-account" title="Profile" to="/profile" />
          <v-list-item prepend-icon="mdi-settings" title="Settings" to="/settings" />
          <v-divider />
          <v-list-item prepend-icon="mdi-logout" title="Sign Out" @click="goToLogin()" />
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer v-model="isDrawerOpen" temporary>
      <v-list-item title="Jara" subtitle="Just Another Recipe App" />
      <v-divider />
      <v-list-item title="About" to="/about" />
      <v-list-item title="Contact" to="/contact" />
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>

    <v-snackbar
      v-model="isNotifyOpen"
      :timeout="$store.getters.notify.timeout"
      :color="$store.getters.notify.type"
      @update:modelValue="val => hideNotify(!val)"
    >
      {{ $store.getters.notify.message }}
      <template v-slot:actions>
        <v-btn color="white" text="Close" @click="hideNotify(true)" />
      </template>
    </v-snackbar>

  </v-app>
</template>

<script>
import { AUTH_CLEAR } from '@/store/types/auth'
import { NOTIFY_HIDE } from '@/store/types/common'

export default {
  data () {
    return {
      isDrawerOpen: false,
      isNotifyOpen: false
    }
  },
  computed: {
    appVersion () {
      return 'v' + process.env.APP_VERSION
    }
  },
  watch: {
    '$store.getters.notify.visible' (newValue, oldValue) {
      this.isNotifyOpen = newValue
    }
  },
  methods: {
    hideNotify (hide) {
      if (hide) {
        this.$store.commit(NOTIFY_HIDE)
      }
    },
    goToLogin () {
      this.$store.commit(AUTH_CLEAR)
      this.$router.push({ path: '/login' })
    }
  }
}
</script>
