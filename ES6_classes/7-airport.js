export default class Airport {
  constructor(name, code) {
    const validateInputs = () => {
      if (typeof code !== 'string' || typeof name !== 'string') {
        throw new Error('Invalid input types');
      }
    };
    validateInputs();
    this._name = name;
    this._code = code;
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

  // Override the toString method to include both the concise and detailed representation
  // Method for the detailed string representation
  detailedToString() {
    return `Airport [${this._code}] { _name: '${this._name}', _code: '${this._code}' }`;
  }

  // Override the toString method for the concise representation
  toString() {
    return `[object ${this._code}]`;
  }
}
