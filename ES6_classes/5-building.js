export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error("Abstract class 'Building' cannot be instantiated.");
    }
    this._sqft = sqft;
  }

  get sqft() { return this._sqft; }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
