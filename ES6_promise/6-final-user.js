// signup.js
import signUpUser from "./4-user-promise"
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then((results) => {
    console.log(`${results[0].firstName} ${results[0].lastName} ${results[1].fileName}`);
  }).catch(() => console.log(''));
}
