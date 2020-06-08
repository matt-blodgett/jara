const version = require('./package.json').version

module.exports = function (ctx) {
  return {
    boot: [
      'axios',
      'components',
      'functions',
      'store',
      'vuelidate',
      'global-vue-config'
    ],
    css: [
      'app.styl'
    ],
    extras: [
      'mdi-v5'
    ],
    // supportIE: true,
    build: {
      modern: true,
      env: {
        VERSION: JSON.stringify(version)
      },
      scopeHoisting: true,
      // vueRouterMode: 'history',
      // vueCompiler: true,
      // gzip: true,
      // analyze: true,
      // extractCSS: false,
      chainWebpack(chain) {
        chain.output.set('globalObject', 'this')
      },
      extendWebpack (cfg) {
        cfg.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules|quasar)/
        })
      },
      transpileDependencies: [
        /[\\/]node_modules[\\/]mem[\\/]/,
        /[\\/]node_modules[\\/]mimic-fn[\\/]/,
        /[\\/]node_modules[\\/]p-is-promise[\\/]/,
        /[\\/]node_modules[\\/]map-age-cleaner[\\/]/,
        /[\\/]node_modules[\\/]p-defer[\\/]/
      ]
    },
    devServer: {
      port: 8888,
      open: true,
      host: '0.0.0.0',
      proxy: {
        '/api': {
          target: 'http://api:8000',
          secure: false,
          changeOrigin: true
        }
      },
      watchOptions: {
        poll: true
      }
    },
    framework: {
      all: false,
      components: [
        'QList',
        'QItem',
        'QItemSection',
        'QItemLabel',
        'QBadge',
        'QBanner',
        'QBar',
        'QBtn',
        'QCard',
        'QCardActions',
        'QCardSection',
        'QDrawer',
        'QFooter',
        'QForm',
        'QHeader',
        'QIcon',
        'QInnerLoading',
        'QInput',
        'QLayout',
        'QPage',
        'QPageContainer',
        'QScrollArea',
        'QSeparator',
        'QSpace',
        'QSpinner',
        'QToolbar',
        'QToolbarTitle'
      ],
      directives: [
        'Ripple'
      ],
      plugins: [
        // 'Dialog',
        'Loading',
        'Notify',
        'LoadingBar'
      ],
      config: {
        loading: {
          spinnerSize: 250,
          spinnerColor: 'white'
        },
        loadingBar: {
          skipHijack: true
        }
      },
      iconSet: 'mdi-v5'
    },
    animations: [],
    ssr: {
      pwa: false
    },
    preloadChunks: false,
    pwa: {
      // workboxPluginMode: 'InjectManifest',
      workboxOptions: {
        skipWaiting: true,
        clientsClaim: true
      },
      manifest: {
        name: 'Just Another Recipe App',
        short_name: 'jara',
        description: 'Just another recipe app',
        display: 'standalone',
        orientation: 'portrait',
        background_color: 'white',
        theme_color: '#027be3',
        start_url: '/index.html',
        icons: [
          {
            'src': '/statics/icons/jara-logo-192x192.png',
            'sizes': '192x192',
            'type': 'image/png'
          },
          {
            'src': '/statics/icons/jara-logo-512x512.png',
            'sizes': '512x512',
            'type': 'image/png'
          },
          {
            'src': '/statics/icons/jara-logo.svg',
            'sizes': 'any',
            'type': 'image/svg+xml'
          }
        ]
      }
    }
  }
}
