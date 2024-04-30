module.exports = {
    presets: [
      ["@babel/preset-env", {
        targets: {
          edge: "17",
          firefox: "60",
          chrome: "67",
          safari: "11.1"
        },
        useBuiltIns: "usage",
        corejs: 3, // Specify the version of core-js
      }]
    ],
    plugins: [
      // List any Babel plugins here if needed
    ]
  };
  
  