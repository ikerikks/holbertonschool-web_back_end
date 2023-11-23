function student(id, firstName, location) {
  return {
    id,
    firstName,
    location,
  };
}

export default function getListStudents() {
  return [
    student(1, 'Guillaume', 'San Francisco'),
    student(2, 'James', 'Columbia'),
    student(5, 'Serena', 'San Francisco'),
  ];
}
