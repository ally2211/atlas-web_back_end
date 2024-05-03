export default class Building {
  constructor(sqft) {
    const validateInputs = () => {
      if (typeof sqft !== 'number') {
        throw new TypeError('sqft must be a number.');
      }
    };
    validateInputs();
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('sqft must be a number.');
    }
    this._sqft = value;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
