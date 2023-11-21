export default function getListStudentsIds(array) {
  return Array.isArray(array) ? array.map(item => item.id):[];
}