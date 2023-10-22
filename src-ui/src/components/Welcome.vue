<template>
  <v-container class="fill-height">
    <div>WELCOME</div>
    <v-btn
      text="GO TO TEST"
      @click="goToTest()"
    />
  </v-container>
</template>

<script>
export default {
  methods: {
    goToTest () {
      this.$router.push({ path: '/test' })
    }
  }
}
</script>
