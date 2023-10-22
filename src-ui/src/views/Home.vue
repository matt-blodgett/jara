<template>
  <div>
    <Welcome />
    <div>{{ $store.getters.isAuthenticated ? 'Authenticated' : 'Not Authenticated' }}</div>
  </div>
</template>

<script>
import Welcome from '@/components/Welcome.vue'

export default {
  components: {
    Welcome
  }
}
</script>
