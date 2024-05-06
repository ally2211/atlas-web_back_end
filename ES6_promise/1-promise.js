// 1-promise.js
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
  if (success) {
    // Resolve the promise with an object
    resolve({
      status: 200,
      body: 'Success'
    });
  } else {
    // Reject the promise with an error
    reject(new Error('The fake API is not working currently'));
  }
  });
}
