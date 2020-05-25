<template>
  <q-page class="items-start">
    <div class="absolute-center text-center">
      <p class="q-display-4 text-weight-regular">401</p>
      <p class="q-display-2 text-faded">Unauthorized</p>
      <p class="text-faded">Access to this page is denied</p>
      <p>
        <q-btn v-text="'Go Home'" color="primary" link to="/" />
      </p>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Error401'
}
</script>

<style scoped lang="stylus">
</style>
