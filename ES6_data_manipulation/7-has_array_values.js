export default function hasValuesFromArray(set, array) {
  let result = false;
  array.forEach((ele) => {
    result = set.has(ele);
  });
  return result;
}
