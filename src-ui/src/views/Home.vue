<template>
  <div>
    <Welcome />
    <div>{{ $store.getters.isAuthenticated ? 'Authenticated' : 'Not Authenticated' }}</div>
    <div>{{ `got version: ${gotVersion}` }}</div>
    <v-btn text="Get version" @click.stop="testApi()" />
  </div>
</template>

<script>
import Welcome from '@/components/Welcome.vue'
import { apiClient } from '@/api'

export default {
  components: {
    Welcome
  },
  data () {
    return {
      gotVersion: null
    }
  },
  methods: {
    testApi () {
      apiClient.get('/version').then(response => {
        this.gotVersion = response.data.version
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
