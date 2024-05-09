export default function divideFunction(numerator, denominator) {
  // Example asynchronous operation
  return new Promise((resolve) => {
    if (denominator === 0) {
      return Promise.reject(new Error('cannot divide by 0'));
    }
    if (numerator && denominator) {
      // Resolve the promise with an object
      const result = numerator / denominator;
      resolve({ result });
    }
    return undefined;
  });
}
