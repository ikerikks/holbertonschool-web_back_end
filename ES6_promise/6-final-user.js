import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise = Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  return promise;
}