// File: 2-hbtn_course.js
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    const validateInputs = () => {
      if (typeof amount !== 'number') {
        throw new TypeError('Amount must be a number.');
      }
      if (!(currency instanceof Currency)) {
        throw new TypeError('Currency must be an instance of Currency.');
      }
    };
    validateInputs();
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Name must be a number.');
    }
    this._amount = value;
  }

  // Getter for currency
  get currency() {
    return this._currency;
  }
  
  // Setter for currency
  set currency(value) {
  if (!(value instanceof Currency)) {
    throw new TypeError('Currency must be an instance of Currency.');
  }
  this._currency = value;
  }

  convertPrice(amount, convert) {
    if (typeof amount !== 'number' || typeof convert !== 'number') {
      throw new Error('Invalid input types');
    }
    return amount * convert;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }
}
