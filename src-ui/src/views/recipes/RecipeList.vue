<template>
  <v-container class="fill-height">
    
    <v-btn text="Load" color="primary" @click="fetchRecipes()" />

    <v-container>
      <v-row>
        <v-col v-for="row in results" :key="row.id" :cols="12">
          <RecipeCard :recipe="row" />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>

<script>
import RecipeCard from './RecipeCard.vue'

export default {
  components: {
    RecipeCard
  },
  data () {
    return {
      count: 0,
      results: []
    }
  },
  methods: {
    fetchRecipes () {
      const url = '/recipes/recipes'
      const params = {
        limit: 10,
        offset: 0
      }
      this.$apiClient.get(url, { params: params }).then(response => {
        this.count = response.data.count
        this.results = response.data.results
      }).catch(() => {
        console.log('error fetching recipes')
      })
    }
  }
}
</script>
