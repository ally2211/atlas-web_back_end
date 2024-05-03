import Building from './5-building';

export default class SkyHighBuilding  extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._sqft = sqft;
    const validateInputs = () => {
      if (typeof floors !== 'number') {
        throw new TypeError('floors must be a number.');
      }
    };
    validateInputs();
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Floors must be a number.');
    }
    this._floors = value;
  }

  // Getter for building
  get building() {
    return this._building;
  }

  // Setter for building
  set building(value) {
    if (!(value instanceof Building)) {
      throw new TypeError('Building must be an instance of Building.');
    }
    this._building = value;
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this._floors} floors`);
}
}