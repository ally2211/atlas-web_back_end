export default function handleResponseFromAPI(promise) {
  if (promise instanceof Promise) {
    return promise.then((response) => {
      console.log('Got a response from the API'); // Log the success message
      return {
        status: 200,
        body: 'success'
      };
    }).catch((error) => {
      throw error; // Re-throw the error to maintain rejection
    });
  } else {
    // If the passed argument is not a promise, reject with an error
    return Promise.reject(new Error());
  }
}
