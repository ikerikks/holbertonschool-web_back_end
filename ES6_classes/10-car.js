export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const constructor = this.constructor[Symbol.species] || this.constructor;
    const newCar = new constructor();
    for (const key of Object.keys(this)) {
      newCar[key] = undefined;
    }

    return newCar;
  }
}
