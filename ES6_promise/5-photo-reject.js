export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    // Check if the filename is not provided
    if (fileName) {
      // Reject the promise with an error
      reject(new Error(`${fileName} cannot be processed`));
    } else {
      // Additional checks can be performed here
      // For example, checking if the file exists in the directory

      // If all checks pass, resolve the promise (example placeholder)
      resolve({ fileName });
    }
  });
}
