export default [
    {
      env: {
        node: true,
        jest: true,
        es2020: true
      },
      extends: [
        'eslint:recommended'
      ],
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: 'module'
      },
      rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'semi': ['error', 'always'],
        'quotes': ['error', 'single'],
        'indent': ['error', 2],
        'comma-dangle': ['error', 'never'],
        'arrow-parens': ['error', 'always'],
        'no-unused-vars': ['warn', { 'argsIgnorePattern': '^_' }],
        'max-len': ['warn', { 'code': 120 }],
        'eol-last': ['error', 'always'],
        'no-multiple-empty-lines': ['error', { 'max': 1, 'maxEOF': 1 }],
        'object-curly-spacing': ['error', 'always'],
        'array-bracket-spacing': ['error', 'never']
      }
    }
  ];
  