// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      // Resolve the promise with a value
      resolve('API response');
    }, 1000); // Simulate a delay
  });
}
