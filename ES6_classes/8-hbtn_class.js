export default class HolbertonClass {
  constructor(size, location) {
    const validateInputs = () => {
      if (typeof size !== 'number') {
        throw new Error('Size must be a number.');
      }
      if (typeof location !== 'string') {
        throw new TypeError('Location must be a string.');
      }
    };
    validateInputs();
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Size must be a number.');
    }
    this._code = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Location must be a string.');
    }
    this._name = value;
  }

  // Override the toString method to include both the concise and detailed representation
  // Method for the detailed string representation
  toString() {
    return `${this._location}`;
  }

  valueOf() {
    return `${this._size}`;
  }
}
