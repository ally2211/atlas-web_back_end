export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error("Building cannot be instantiated directly");
    }
    this._validateSqft(sqft);
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._validateSqft(value);
    this._sqft = value;
  }

  _validateSqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number.');
    }
  }

  evacuationWarningMessage() {
    throw new Error("Class extending Building must override evacuationWarningMessage");
  }
}
