export default function handleResponseFromAPI(promise) {
  promise
    .then((data) => {
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch((err) => {
      return new Error();
    })
    .finally((data) => {
      console.log('Got a respponse from the API');
    })
}
