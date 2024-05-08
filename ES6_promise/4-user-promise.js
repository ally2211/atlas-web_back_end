export default function handlePrsignUpUser(firstName, lastName) {
  // Example asynchronous operation
  return new Promise((resolve) => {
    if (firstName && lastName) {
      // Resolve the promise with an object
      resolve({
        firstName: firstName,
        lastName: lastName,
      });
    }
  });
}
