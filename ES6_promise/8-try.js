export default function divideFunction(numerator, denominator) {
  // Example asynchronous operation
  return new Promise((resolve) => {
    if (numerator && denominator) {
      // Resolve the promise with an object
      resolve({
        numerator,
        denominator,
      });
    }
  });
}
