export default class Car {
  constructor(brand, motor, color) {
    const validateInputs = () => {
      if (typeof brand !== 'string' || typeof motor !== 'string' || typeof color !== 'string') {
        throw new Error('Invalid input types');
      }
    };
    validateInputs();
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  set brand(value) {
    if (typeof value !== 'string') {
      throw new TypeError('brand must be a string.');
    }
    this._brand = value;
  }

  get motor() {
    return this._motor;
  }

  set motor(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Motor must be a string.');
    }
    this._motor = value;
  }

  get color() {
    return this._color;
  }

  set color(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Color must be a string.');
    }
    this._color = value;
  }

  // Override the toString method to include both the concise and detailed representation
  // Method for the detailed string representation
  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }
}
