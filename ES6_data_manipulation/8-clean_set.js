export default function cleanSet(set, startString) {
  if(typeof startString === 'string' && startString.length > 0) {
    return new Array(...set).filter(word => word.includes(startString)).map((str) => str.split(startString).join('')).join('-');
  } else {
    return '';
  }
}
