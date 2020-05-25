module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        "modules": "commonjs",
        "loose": false,
        "useBuiltIns": "usage",
        "corejs": '2.0.0',
      }
    ]
  ],
  plugins: [
    [
      "@babel/transform-runtime",
      {
        "regenerator": false
      }
    ],
    "@babel/plugin-syntax-dynamic-import",
    "@babel/plugin-syntax-import-meta",
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-json-strings",
    [
      "@babel/plugin-proposal-decorators",
      {
        "legacy": true
      }
    ],
    "@babel/plugin-proposal-function-sent",
    "@babel/plugin-proposal-export-namespace-from",
    "@babel/plugin-proposal-numeric-separator",
    "@babel/plugin-proposal-throw-expressions"
  ],
  comments: false
}
