<template>
  <q-page padding>
    <div>{{ `User ID: ${$store.getters.userProfile.user_id}` }}</div>
    <div>{{ `First Name: ${$store.getters.userProfile.first_name}` }}</div>
    <div>{{ `Last Name: ${$store.getters.userProfile.last_name}` }}</div>
  </q-page>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped lang="stylus">
</style>
