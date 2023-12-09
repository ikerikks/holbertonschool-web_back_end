// 3-all.js
import { uploadPhoto, createUser } from './utils.js   ';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoData, userData]) => {
      const { firstName } = userData;
      const { lastName } = userData;
      console.log(`${photoData.body} ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
