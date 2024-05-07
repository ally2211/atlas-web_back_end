export default function handleResponseFromAPI(promise) {
  if (promise instanceof Promise) {
    return promise.then(() => {
      console.log('Got a response from the API'); // Log the success message
      return {
        status: 200,
        body: 'success',
      };
    }).catch((error) => {
      return Promise.reject(new Error());
    });
  }
}
