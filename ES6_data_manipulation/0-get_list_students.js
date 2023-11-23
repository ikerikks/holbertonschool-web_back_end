function student(id, firstName, location) {
  return {
    id: id,
    firstName: firstName,
    location: location,
  };
}

export default function getListStudent() {
  return [
    student(1, 'Guillaume', 'San Francisco'),
    student(2, 'James', 'Columbia'),
    student(5, 'Serena', 'San Francisco'),
  ];
}
