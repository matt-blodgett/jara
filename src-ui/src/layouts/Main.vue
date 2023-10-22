<template>
  <v-app>
    <v-app-bar color="primary" prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="isDrawerOpen = !isDrawerOpen" />
      <v-toolbar-title>Jara</v-toolbar-title>
      <v-spacer />
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon="mdi-dots-vertical" v-bind="props" />
        </template>
        <v-list>
          <v-list-item prepend-icon="mdi-account" title="Sign Out" @click.stop="signOut()" />
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer v-model="isDrawerOpen" temporary>
      <v-list-item title="Jara" subtitle="Just Another Recipe App" />
      <v-divider />
      <v-list-item title="Sign In" to="/login" />
      <v-list-item title="Test" to="/test" />
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      isDrawerOpen: false
    }
  },
  methods: {
    signOut () {
      console.log('signed out')
    }
  }
}
</script>
