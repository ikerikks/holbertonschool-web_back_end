export default function hasValuesFromArray(set, array) {
  return array.reduce((hasValues, value) => {
    hasValues = set.has(value);
    return hasValues;
  }, false);
}
