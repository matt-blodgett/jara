<template>
  <v-container class="fill-height">

    <v-sheet :border="true" class="pa-6 mx-auto" rounded :width="500">

      <h2 class="text-h5 mb-6">Create Recipe</h2>

      <v-alert
        class="my-6"
        closable
        color="error"
        icon="$error"
        title="Saving failed"
        text="There was an error saving your recipe"
        v-model="isErrorSubmit"
      />

      <v-form ref="form" fast-fail @submit.prevent="submit">

        <v-text-field
          label="Title"
          required
          :counter="100"
          v-model="recipe.title"
        />

        <v-text-field
          label="Description"
          required
          :counter="2048"
          v-model="recipe.description"
        />

        <v-text-field
          label="Notes"
          required
          :counter="4096"
          v-model="recipe.notes"
        />

        <v-divider class="mb-4" />

        <v-container>
          <v-row v-for="(ingredient, index) in recipe.ingredients" :key="`ingredient-${index}`">
            <v-col>
              <div>{{ `#${index}` }}</div>
            </v-col>
            <v-col>
              <div>{{ ingredient.quantity }}</div>
            </v-col>
            <v-col>
              <div>{{ ingredient.unit_of_measure }}</div>
            </v-col>
            <v-col>
              <div>{{ ingredient.name }}</div>
            </v-col>
            <v-col>
              <v-btn label="del" color="negative" @click="removeIngredient(index)" />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn label="add" color="primary" @click="appendIngredient()" />
            </v-col>
          </v-row>
        </v-container>

        <v-divider class="mb-4" />

        <v-container>
          <v-row v-for="(instruction, index) in recipe.instruction" :key="`instruction-${index}`">
            <v-col>
              <div>{{ `#${index}` }}</div>
            </v-col>
            <v-col>
              <div>{{ instruction.text }}</div>
            </v-col>
          </v-row>
        </v-container>        

        <div class="text-center">
          <v-btn color="primary" text="Submit" @click="submit()" :loading="isLoadingSubmit" />
        </div>

      </v-form>

    </v-sheet>

  </v-container>
</template>

<script>
export default {
  data () {
    return {
      isLoadingSubmit: false,
      isErrorSubmit: false,
      recipe: {
        title: null,
        description: null,
        notes: null,
        ingredients: [
          {
            quantity: null,
            unit_of_measure: null,
            name: null
          }
        ],
        instructions: [
          {
            text: null
          }
        ]
      }
    }
  },
  computed: {
  },
  methods: {
    appendIngredient () {
      this.recipe.ingredients.push({
        quantity: null,
        unit_of_measure: null,
        name: null
      })
    },
    removeIngredient (index) {
      this.recipe.ingredients.splice(index, 1)
    },
    async submit () {
      const { valid } = await this.$refs.form.validate()
      if (valid) {
        // this.isErrorSubmit = false
        // this.isLoadingSubmit = true
        // this.$store.dispatch(AUTH_REQUEST, this.formData).then(response => {
        //   this.isLoadingSubmit = false
        //   this.$store.commit(NOTIFY_SHOW, {
        //     type: 'success',
        //     message: 'Login successful'
        //   })
        //   this.$router.push({ path: '/home' })
        // }).catch(error => {
        //   this.isErrorSubmit = true
        //   this.isLoadingSubmit = false
        //   this.$store.commit(NOTIFY_SHOW, {
        //     type: 'error',
        //     message: 'Login failed'
        //   })
        // })
      }
    }
  },
  mounted () {
  }
}
</script>
