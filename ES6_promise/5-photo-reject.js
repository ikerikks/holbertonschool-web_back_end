export default function uploadPhoto(fileName) {
  return new Promise(function(_, reject) {
    reject(new Error(`${fileName} cannot be processed`))
  });
}
