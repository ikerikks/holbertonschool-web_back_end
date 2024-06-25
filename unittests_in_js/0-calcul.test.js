import assert from 'assert';
import { calculateNumber } from './0-calcul.js';

describe('calculateNumber', () => {
  it('should return the sum of an operation', () => {
    assert(calculateNumber(2, 2), 4);
  });
});

