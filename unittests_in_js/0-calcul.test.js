const assert = require('assert');
const { calculateNumber } = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('should return the sum of an operation', () => {
    assert.equal(calculateNumber(2, 2), 4);
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1.6, 1.8), 4);
    assert.equal(calculateNumber(1.7, 1.2), 3);
    assert.strictEqual(calculateNumber(1, 3.9), 5);
    assert.strictEqual(isNaN(calculateNumber(1,)), true);
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(0, 1.2), 1);
    assert.equal(calculateNumber(1.3, 1.3), 2);
    assert.equal(calculateNumber(1.7, 1.2), 3);
    assert.equal(calculateNumber(1.3, 1.8), 3);
    assert.equal(calculateNumber(1.6, 1.8), 4);
    assert.equal(calculateNumber(0, 1.0), 1);
    assert.equal(calculateNumber(0, 1.3), 1);
    assert.equal(calculateNumber(0, 1.7), 2);
    assert.equal(calculateNumber(1.0, 0), 1);
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(1.7, 0), 2);
  });
});

