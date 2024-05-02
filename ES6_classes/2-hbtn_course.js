// File: 2-hbtn_course.js

export default class HolbertonCourse {
  constructor(name, length, students) {
    const validateInputs = () => {
      if (typeof name !== 'string' || typeof length !== 'number' || !Array.isArray(students) || !students.every(student => typeof student === 'string')) {
        throw new Error('Invalid input types');
      }
     };
    validateInputs();
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string.');
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number.');
    }
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    const setStudents = (value) => {
      if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings.');
      }
      this._students = value;
    };
    setStudents(value);
  }
}
