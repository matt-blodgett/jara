<template>
  <q-layout view="hhh lpr fff">

    <q-header>
      <q-bar>
        <q-space />
        <q-badge transparent color="primary">{{ appVersion }}</q-badge>
      </q-bar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  name: 'TopLayoutLogin',
  computed: {
    appVersion: function () {
      return 'v' + process.env.VERSION
    }
  }
}
</script>

<style scoped lang="stylus">
</style>
