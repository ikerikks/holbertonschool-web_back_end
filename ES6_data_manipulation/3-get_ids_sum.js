export default function getStudentIdsSum(array) {
  return array.reduce((sum, student) => sum + student.id, 0);
}
