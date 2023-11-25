// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    themes: {
      light: {
        colors: {
          primary: '#1867C0',
          secondary: '#5CBBF6',
          success: '#8BC34A',
          error: '#F44336',
          warning: '#FFC107',
          info: '#2196F3',
        },
      },
    },
  },
  defaults: {
    VTextField: {
      variant: 'outlined',
      density: 'compact',
    },
    VTextarea: {
      variant: 'outlined'
    },
  },
})
