const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calcul test', () => {
  it('checks sum of int', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
});

describe('calcul test', () => {
  it('checks sum is rounded', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
});

describe('calcul test', () => {
  it('checks sum is rounded with 2 numbers after coma', () => {
    assert.equal(calculateNumber(1.25, 3.75), 5);
  });
});

describe('calcul test', () => {
  it('checks a is rounded', () => {
    assert.equal(calculateNumber(1.6, 3), 5);
  });
});

describe('calcul test', () => {
  it('checks b is rounded', () => {
    assert.equal(calculateNumber(1, 3.6), 5);
  });
});

describe('calcul test', () => {
  it('checks a long float are rounded', () => {
    assert.equal(calculateNumber(1.665897, 3.895477656), 6);
  });
});

describe('calcul test', () => {
  it('test sum of negative numbers', () => {
    assert.equal(calculateNumber(-1, -3), -4);
  });
});

describe('calcul test', () => {
  it('test sum with a is negative', () => {
    assert.equal(calculateNumber(-1, 3), 2);
  });
});

describe('calcul test', () => {
  it('test sum with b is negative', () => {
    assert.equal(calculateNumber(1, -3), -2);
  });
});

describe('calcul test', () => {
  it('test sum with a is negative and float', () => {
    assert.equal(calculateNumber(-1.56, 3), 1);
  });
});

describe('calcul test', () => {
  it('test sum with b is negative and float', () => {
    assert.equal(calculateNumber(1, -3.2), -2);
  });
});

describe('calcul test', () => {
  it('should test a et b = 0', () => {
    assert.equal(calculateNumber(0, 0), 0);
  });
});

describe('calcul test', () => {
  it('should test a et b = infinity', () => {
    assert.equal(calculateNumber(Infinity, Infinity), Infinity);
  });
});

describe('calcul test', () => {
  it('should test a = 1 et b = infinity', () => {
    assert.equal(calculateNumber(1, Infinity), Infinity);
  });
});

describe('calcul test', () => {
  it('should test a = infinity et b = 1', () => {
    assert.equal(calculateNumber(Infinity, 1), Infinity);
  });
});

describe('calcul test', () => {
  it('should test a = -infinity et b = 1', () => {
    assert.equal(calculateNumber(-Infinity, 1), -Infinity);
  });
});

describe('calcul test', () => {
  it('should test a = -0 et b = 1', () => {
    assert.equal(calculateNumber(-0, 1), 1);
  });
});

describe('calcul test', () => {
  it('should test a = NaN et b = 1', () => {
    assert(isNaN(calculateNumber(NaN, 1)));
  });
});

describe('calcul test', () => {
  it('should test a = NaN et b = NaN', () => {
    assert(isNaN(calculateNumber(NaN, NaN)));
  });
});

describe('calcul test', () => {
  it('should test a = 0 et b = 0', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
});

describe('calcul test', () => {
  it('should test a = 0 et b = 0', () => {
    assert.strictEqual(calculateNumber(0.2, 0.4), 0);
  });
});