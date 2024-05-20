import Building from './5-building.js';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  // super.evacuationWarningMessage() {
  //   return `Evacuate slowly the ${this.floors} floors`;
  // })
  evacuationWarningMessage = ()=> `Evacuate slowly the ${this.floors} floors`;

}

export default SkyHighBuilding;
