import * as util from './utils.js';
export default function handleProfileSignup() {
  const promise1 = util.uploadPhoto()
  const promise2 = util.createUser()
  Promise.all([promise1, promise2])
    .then((data) => {
      const newData = {};
      data.forEach((obj) => Object.assign(newData, obj));
      let result = Object.values(newData)
        .filter((val) => typeof val != 'number' )
        .join(' ');
      console.log(result);
    })
    .catch((err) => console.log('Signup system offline'))
}
