export default function getStudentIds(array) {
  return Array.isArray(array) ? array.map(student => student.id) : [];
}
