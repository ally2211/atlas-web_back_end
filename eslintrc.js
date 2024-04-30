// Importing using CommonJS syntax
const globals = require('globals');
const { configs } = require('@eslint/js');

module.exports = {
  // Applying global variables
  globals: globals.browser,

  // ESLint built-in recommended configurations
  extends: [
    "eslint:recommended",
    configs.recommended  // This assumes @eslint/js exports a 'recommended' config
  ],

  // Additional ESLint rules and configurations
  rules: {
    'indent': ['error', 2],
    'semi': ['error', 'always'],
    'no-unused-vars': ['warn']
  },

  // Parser options to define ECMAScript support
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  },

  // Define environment settings
  env: {
    browser: true,
    es2021: true,
    node: true
  }
};
