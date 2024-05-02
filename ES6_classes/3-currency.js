// File: 2-hbtn_course.js

export default class Currency {
  constructor(code, name) {
    const validateInputs = () => {
      if (typeof code !== 'string' || typeof name !== 'string') {
        throw new Error('Invalid input types');
      }
    };
    validateInputs();
    this._code = code;
    this._name = name;
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

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string.');
    }
    this._code = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
