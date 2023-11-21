export default function getStudentIdsSum(array) {
  return array.reduce((total, student) => {
    return total + student.id; 
  }, 0)
}