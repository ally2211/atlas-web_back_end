// 2=then.js
export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (promise) {
      // Resolve the promise with an object
      resolve({
        status: 200,
        body: 'Success',
      });
      console.log('Got a response from the API');
    } else {
      // Reject the promise with an error
      reject(new Error());
      console.log('Signup system offline');
    }
  });
}
