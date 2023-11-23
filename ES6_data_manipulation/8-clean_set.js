export default function cleanSet(set, startString) {
  return new Array(...set).filter(word => word.includes(startString)).map((str) => str.split(startString).join('')).join('-');
}
