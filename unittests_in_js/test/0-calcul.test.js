// test/rounding.test.js
const assert = require('assert');
const calculateNumber = require('../0-calcul.js');

describe('calculateNumber', function () {
  it('should return the sum of the rounded numbers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4); 
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(2, 2.6), 5);
  });
  describe('Rounding the second number', function () {
    it('should correctly round the second number up', function () {
      assert.strictEqual(calculateNumber(1, 2.8), 4); // 1 + 3
    });

    it('should correctly round the second number down', function () {
      assert.strictEqual(calculateNumber(1, 2.2), 3); // 1 + 2
    });
  });
});


