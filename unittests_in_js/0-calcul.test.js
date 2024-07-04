const assert = require('assert');
const { calculateNumber } = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('it round the first argument', () => {
    assert.equal(calculateNumber(1.0, 0), 1);
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(1.7, 0), 2);
  });

  it('it round the second argument', () => {
    assert.equal(calculateNumber(0, 1.0), 1);
    assert.equal(calculateNumber(0, 1.3), 1);
    assert.equal(calculateNumber(0, 1.7), 2);
  });

  it('it should return the right number', () => {
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(0, 1.2), 1);
    assert.equal(calculateNumber(1.3, 1.3), 2);
    assert.equal(calculateNumber(1.7, 1.2), 3);
    assert.equal(calculateNumber(1.3, 1.8), 3);
    assert.equal(calculateNumber(1.6, 1.8), 4);
  
  });

});


// describe('calculateNumber', () => {
//   it('should return the sum of an operation', () => {
//     assert.equal(calculateNumber(2, 2), 4);
//     assert.strictEqual(calculateNumber(1, 3), 4);
//     assert.strictEqual(calculateNumber(1.6, 1.8), 4);
//     assert.equal(calculateNumber(1.7, 1.2), 3);
//     assert.strictEqual(calculateNumber(1, 3.9), 5);
//     assert.strictEqual(isNaN(calculateNumber(1,)), true);
//     assert.equal(calculateNumber(1.3, 0), 1);
//     assert.equal(calculateNumber(0, 1.2), 1);
//     assert.equal(calculateNumber(1.3, 1.3), 2);
//     assert.equal(calculateNumber(1.7, 1.2), 3);
//     assert.equal(calculateNumber(1.3, 1.8), 3);
//     assert.equal(calculateNumber(1.6, 1.8), 4);
//     assert.equal(calculateNumber(0, 1.0), 1);
//     assert.equal(calculateNumber(0, 1.3), 1);
//     assert.equal(calculateNumber(0, 1.7), 2);
//     assert.equal(calculateNumber(1.0, 0), 1);
//     assert.equal(calculateNumber(1.3, 0), 1);
//     assert.equal(calculateNumber(1.7, 0), 2);
//   });
//   it('should return 0 when inputs are -0.4 and 0.4', () => {
//     const result = calculateNumber(-0.4, 0.4);
//     console.log(`calculateNumber(-0.4, 0.4) = ${result}`);
//     assert.strictEqual(result, 0);
//   });
//   it('should return -1 when inputs are -0.7 and -0.4', () => {
//     const result = calculateNumber(-0.7, -0.4);
//     console.log(`calculateNumber(-0.7, -0.4) = ${result}`);
//     assert.strictEqual(result, -1);
//   });
//   it('should return 5 when inputs are 1 and 3.7', () => {
//     const result = calculateNumber(1, 3.7);
//     console.log(`calculateNumber(1, 3.7) = ${result}`);
//     assert.strictEqual(result, 5);
//   });

//   it('should return 5 when inputs are 1.2 and 3.7', () => {
//     const result = calculateNumber(1.2, 3.7);
//     console.log(`calculateNumber(1.2, 3.7) = ${result}`);
//     assert.strictEqual(result, 5);
//   });

//   it('should return 6 when inputs are 1.5 and 3.7', () => {
//     const result = calculateNumber(1.5, 3.7);
//     console.log(`calculateNumber(1.5, 3.7) = ${result}`);
//     assert.strictEqual(result, 6);
//   });

//   // Additional test cases
//   it('should return 0 when inputs are 0.1 and -0.1', () => {
//     const result = calculateNumber(0.1, -0.1);
//     console.log(`calculateNumber(0.1, -0.1) = ${result}`);
//     assert.strictEqual(result, 0);
//   });

//   it('should return -4 when inputs are -1.4 and -2.6', () => {
//     const result = calculateNumber(-1.4, -2.6);
//     console.log(`calculateNumber(-1.4, -2.6) = ${result}`);
//     assert.strictEqual(result, -4);
//   });

//   it('should return -5 when inputs are -1.5 and -3.5', () => {
//     const result = calculateNumber(-1.5, -3.5);
//     console.log(`calculateNumber(-1.5, -3.5) = ${result}`);
//     assert.strictEqual(result, -6);
//   });

//   it('should return 5 when inputs are 2.4 and 2.5', () => {
//     const result = calculateNumber(2.4, 2.5);
//     console.log(`calculateNumber(2.4, 2.5) = ${result}`);
//     assert.strictEqual(result, 5);
//   });

//   it('should return -4 when inputs are -1.4 and -2.6', () => {
//     const result = calculateNumber(-1.4, -2.6);
//     console.log(`calculateNumber(-1.4, -2.6) = ${result}`);
//     assert.strictEqual(result, -4);
//   });

//   it('should return 10 when inputs are 4.9 and 5.1', () => {
//     const result = calculateNumber(4.9, 5.1);
//     console.log(`calculateNumber(4.9, 5.1) = ${result}`);
//     assert.strictEqual(result, 10);
//   });
// });

