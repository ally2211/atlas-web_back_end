// 6-final-user.js
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Simulate a successful signup
  const signUpResult = signUpUser(firstName, lastName);
  // Simulate a failed photo upload
  const uploadResult = uploadPhoto(fileName).catch(() => `Error: ${fileName} cannot be processed`);
  // Return a promise that resolves to an array of results
  return Promise.all([signUpResult, uploadResult]).then((results) => results.map((result) => ({
    status: result.status, // Assuming result.status is 'fulfilled' or 'rejected'
    value: result.value, // Assuming result.value contains the actual result
  })));
}
