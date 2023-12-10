// 3-all.js
import { uploadPhoto, createUser } from './utils.js   ';

export default function handleProfileSignup() {
  const mergePromise = Promise.all([uploadPhoto(), createUser()]);

  return Promise.resolve()
    .then(() => Promise.all([uploadPhoto(), createUser()]))
    .then(([dataPhoto, dataUser]) => { 
      console.log(dataPhoto.body + ' ' + dataUser.firstName + ' ' + dataUser.lastName);
    })
    .catch(() => { 
      console.log('Signup system offline');
      throw new Error('Signup system offline');
  });

}
