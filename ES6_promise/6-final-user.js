// signup.js
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then((results) => {
    const { status } = results[0]; // Assuming status is a property of the result from signUpUser
    const user = {
      status,
      firstName,
      lastName,
    };
    console.log(`${user.firstName} ${user.lastName}`);
    return user;
  }).catch(() => console.log(''));
}
