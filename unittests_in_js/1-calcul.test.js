const assert = require('assert');
const { calculateNumber } = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('return a sum', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('return a substraction)', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('return a division', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.3);
  });
  it('return an error', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
