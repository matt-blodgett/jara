<template>
  <q-page class="items-start">
    <div class="absolute-center text-center">
      <p class="q-display-4 text-weight-regular">404</p>
      <p class="q-display-2 text-faded">Page not found</p>
      <p class="text-faded">The requested page does not exist</p>
      <p>
        <q-btn v-text="'Go Home'" color="primary" link to="/" />
      </p>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Error404'
}
</script>

<style scoped lang="stylus">
</style>
