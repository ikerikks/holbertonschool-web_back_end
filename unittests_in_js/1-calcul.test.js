import assert from 'assert';
import { calculateNumber } from ('./1-calcul.js');

describe('calculateNumber', () => {
  it('return a sum', () => {
    assert(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('return a substraction)', () => {
    assert(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('return a division', () => {
    assert(calculateNumber('DIVIDE', 1.4, 4.5), 0.3);
  });
  it('return an error', () => {
    assert(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
