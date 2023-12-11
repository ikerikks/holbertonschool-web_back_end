import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const firstPromise = signUpUser(firstName, lastName);
  const secondPromise = uploadPhoto(fileName);
  const promise = Promise.allSettled([firstPromise, secondPromise]);

  promise
    .then((data) => {
      const newData = data;
      newData[1].value = newData[1].reason;
      delete newData[1].reason;
    });

  return promise;
}
