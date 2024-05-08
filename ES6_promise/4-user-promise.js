export default function handlePrsignUpUser(firstName, lastName) {
  // Example asynchronous operation
  return new Promise((resolve, reject) => {
    if (firstName && lastName) {
      // Resolve the promise with an object
      resolve({
        firstName: 'Bob',
        lastName: 'Dylan',
      });
    } else {
      // Reject the promise with an error
      reject(new Error());
    }
  });
}
