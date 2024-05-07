// 2=then.js
export default function handleResponseFromAPI(promise) {
  if (promise instanceof Promise) {
    return new Promise((resolve, reject) => {
      promise.then(() => {
        resolve({
          status: 200,
          body: 'Success'
        });
      }).catch((error) => {
        reject(error);
      });
    });
    } else {
      // If the passed argument is not a promise, reject the new promise with an error
      return Promise.reject(new Error());
    };
}
