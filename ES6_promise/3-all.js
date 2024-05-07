// signup.js
import { uploadPhoto, createUser } from './utils.js'; // Adjust the path as necessary

export default function handleProfileSignup() {
 // Collect all promises
 const promises = [uploadPhoto(), createUser()];

 // Use Promise.all to wait for all promises to resolve
 Promise.all(promises)
    .then((results) => {
      // results is an array of resolved values
      // Assuming the first result is from uploadPhoto and the second is from createUser
      const photoResult = results[0];
      const userResult = results[1];

      // Log the body, firstName, and lastName to the console
      console.log(photoResult.body, userResult.firstName, userResult.lastName);
    })
    .catch((error) => {
      // Log the error message to the console
      console.log('Signup system offline');
    });
}
