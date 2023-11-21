
const getStudent = (id, firstName, location) => {
  return {
    "id": id,
    "firstName": firstName,
    "location": location,
  }
}

export default function getListStudents() {
  return [
    getStudent(1, "Guillaume", "San Francisco"),
    getStudent(2, "James", "Columbia"),
    getStudent(5, "Serena", "San Francisco")
  ];
}