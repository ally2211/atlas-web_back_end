// 1-promise.js
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      // Resolve the promise with an object
      resolve({
        status: 200,
        body: 'success',
      });
      console.log('Got a response from the API');
    } else {
      // Reject the promise with an error
      console.log('Signup system offline');
      reject(new Error());
    }
  });
}
