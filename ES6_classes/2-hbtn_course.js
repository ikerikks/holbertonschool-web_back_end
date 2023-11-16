export default class HolbertonCourse {
  
  constructor(name, length, students) {
    if ( typeof name === "string" || typeof length === "number" ||
          Array.isArray(students)) {
            this._name = name;
            this._length = length;
            this._students = students;
          }
    }
  
  get name() { return this._name; }
  set name(name) { 
    if (typeof name !== "string") {
      console.error("TypeError: Name must be a string");
    }
    this._name = name;
  }
  
  get length() { return this._length; }
  set length(length) {
    if (typeof length !== "number") {
      console.error("TypeError: Length must be a number");
    } 
    this._length = length;
  }

  get students() { return this._students; }
  set students(students) { 
    if (Array.isArray(students)) {
      console.error("TypeError: students must be an array");
    }
    this._students = students; }
}
