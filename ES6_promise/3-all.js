import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const mergePromise = Promise.all([uploadPhoto(), createUser()]);

  return mergePromise
    .then(([dataPhoto, dataUser]) => {
      console.log(`${dataPhoto.body} ${dataUser.firstName} ${dataUser.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
