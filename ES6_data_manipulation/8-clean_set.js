export default function cleanSet(set, startString) {
  if (typeof startString === 'string' && startString.length > 0) {
    return [...set].filter((str) => str !== undefined && str.startsWith(startString))
    .map((str) => str.slice(startString.length)).join('-');
  }
  
  return '';
}
