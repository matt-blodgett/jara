<template>
  <v-app>

    <v-app-bar color="primary" prominent>
      <v-toolbar-title>Jara</v-toolbar-title>
      <div>{{ appVersion }}</div>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>

    <v-footer>
      <v-row justify="center" no-gutters>
        <v-btn
          v-for="link in footerLinks"
          :key="link.to"
          :to="link.to"
          :text="link.text"
        />
        <v-col class="text-center mt-4" cols="12">
          <div>2023 - Jara</div>
        </v-col>
      </v-row>
    </v-footer>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      footerLinks: [
        { text: 'About', to: '/about' },
        { text: 'Contact', to: '/contact' }
      ]
    }
  },
  computed: {
    appVersion () {
      return 'v' + process.env.APP_VERSION
    }
  }
}
</script>
