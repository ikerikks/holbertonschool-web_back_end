export default function getStudentByLocation(array, city) {
  return array.filter((student) => student.location == city);
}
