export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (let ele of array) {
    ele = appendString + ele;
    newArray.push(ele);
  }
  return newArray;
}
