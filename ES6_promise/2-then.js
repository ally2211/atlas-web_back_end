export default function handleResponseFromAPI(promise) {
  if (!(promise instanceof Promise)) {
    // If the passed argument is not a promise, reject with an error
    return Promise.reject(new Error());
  }

  return promise.then(() => {
    console.log('Got a response from the API'); // Log the success message
    return {
      status: 200,
      body: 'success',
    };
  }).catch((_error) => new Error());
}
