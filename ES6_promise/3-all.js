// 3-all.js
import { uploadPhoto, createUser } from './utils.js   ';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoData, userData]) => {
      const { firstName } = userData;
      const { lastName } = userData;
      const result = `${photoData.body} ${firstName} ${lastName}`
      console.log(result);

    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
