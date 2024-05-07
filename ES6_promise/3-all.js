// signup.js
//import { uploadPhoto, createUser } from './utils.js'; // Adjust the path as necessary
import * as utilsFunctions from "./utils";

export default function handleProfileSignup() {
 // Collect all promises
 const promises = [utilsFunctions.uploadPhoto(), utilsFunctions.createUser()];

 // Use Promise.all to wait for all promises to resolve
 Promise.all(promises)
    .then((results) => {
      // results is an array of resolved values
      // Assuming the first result is from uploadPhoto and the second is from createUser
      const photoResult = results[0];
      const userResult = results[1];
      // Log the body, firstName, and lastName to the console
      console.log(`${photoResult.body} ${userResult.firstName} ${userResult.lastName}`);
    })
    .catch(() => new Error('Signup system offline'));
}
