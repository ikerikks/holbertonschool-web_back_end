const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('should return the sum of an operation', () => {
    assert(calculateNumber(2, 2), 4);
  });
});
