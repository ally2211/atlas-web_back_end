// test/rounding.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');
describe('calculateNumber', function () {
  describe('Sum operation', function () {
    it('should return the sum of the rounded numbers', function () {
      assert.strictEqual(calculateNumber('Sum', 4.6, 5.3), 10); // 5 + 5
      assert.strictEqual(calculateNumber('Sum', 4.4, 5.1), 9);  // 4 + 5
    });
  });

  describe('Subtract operation', function () {
    it('should return the difference of the rounded numbers', function () {
      assert.strictEqual(calculateNumber('Subtract', 5.6, 2.2), 4); // 6 - 2
      assert.strictEqual(calculateNumber('Subtract', 4.4, 5.1), -1); // 4 - 5
    });
  });

  describe('Divide operation', function () {
    it('should return the quotient of the rounded numbers', function () {
      assert.strictEqual(calculateNumber('Divide', 8.6, 2.2), 4); // 9 / 2
      assert.strictEqual(calculateNumber('Divide', 5.4, 2.5), 2); // 5 / 2
    });

    it('should throw an error when dividing by zero', function () {
      assert.throws(() => calculateNumber('Divide', 5, 0), /Cannot divide by zero/);
    });
  });

  describe('Invalid operation type', function () {
    it('should throw an error for an invalid operation type', function () {
      assert.throws(() => calculateNumber('Multiply', 4, 5), /Invalid operation type/);
    });
  });
});