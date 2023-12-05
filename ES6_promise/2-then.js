export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch(() => {
      return new Error();
    })
    .finally((data) => {
      console.log('Got a respponse from the API');
    })
}
