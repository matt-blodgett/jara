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
          v-model="recipe.title"
          :maxlength="100"
          counter
          density="compact"
          variant="outlined"
        />

        <v-text-field
]         label="Description"
          v-model="recipe.description"
          :maxlength="2048"
          counter
          density="compact"
          variant="outlined"
        />

        <v-text-field
          label="Notes"
          v-model="recipe.notes"
          :maxlength="4096"
          counter
          density="compact"
          variant="outlined"
        />

        <v-divider class="mb-4" />

        <v-container>
          <v-row v-for="(ingredient, index) in recipe.ingredients" :key="ingredient.id">
            <v-col>
              <div>{{ `#${index}` }}</div>
            </v-col>
            <v-col>
              <v-text-field
                label="Quantity"
                v-model="ingredient.quantity"
                density="compact"
                variant="outlined"
              />
            </v-col>
            <v-col>
              <v-text-field
                label="UOM"
                v-model="ingredient.unit_of_measure"
                density="compact"
                variant="outlined"
              />
            </v-col>
            <v-col>
              <v-text-field
                label="Ingredient Name"
                v-model="ingredient.name"
                density="compact"
                variant="outlined"
              />
            </v-col>
            <v-col>
              <v-btn icon="mdi-delete" color="error" variant="outlined" @click="removeIngredient(index)" />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn icon="mdi-plus-circle-outline" color="success" @click="appendIngredient()" />
            </v-col>
          </v-row>
        </v-container>

        <v-divider class="mb-4" />

        <v-container>
          <v-row v-for="(instruction, index) in recipe.instruction" :key="instruction.id">
            <v-col>
              <div>{{ `#${index}` }}</div>
            </v-col>
            <v-col>
              <v-text-field
                label="Instruction"
                v-model="instruction.text"
                density="compact"
                variant="outlined"
              />
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
