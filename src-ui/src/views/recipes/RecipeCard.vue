<template>
  <v-card class="mx-auto pa-2" border="md" rounded="lg" hover>

    <v-img class="align-end" height="200" src="/src/assets/no-image.svg" />

    <v-card-title>{{ recipe.title }}</v-card-title>

    <v-card-subtitle class="pt-4">{{ `By ${recipe.created_by}` }}</v-card-subtitle>
    <v-card-subtitle class="pt-4">{{ `On ${recipe.created_at}` }}</v-card-subtitle>

    <v-card-text>
      <div>{{ recipe.description }}</div>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart" />
      <v-btn size="small" color="surface-variant" variant="text" icon="mdi-bookmark" />
      <v-btn size="small" color="surface-variant" variant="text" icon="mdi-share-variant" />
    </v-card-actions>

  </v-card>
</template>

<script>
export default {
  props: {
    recipe: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>
