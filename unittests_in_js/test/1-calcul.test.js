// test/rounding.test.js
const assert = require('assert');
const calculateNumber = require('../1-calcul.js');

describe('calculateNumber', function () {
        describe('Sum operation', function () {
        it('should return the sum of the rounded numbers', function () {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6); // 5 + 5
        });
        });

        describe('Subtract operation', function () {
        it('should return the difference of the rounded numbers', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4); // 6 - 2
        });
        });

        describe('Divide operation', function () {
        it('should throw an error when dividing by zero', function () {
            assert.throws(() => calculateNumber('DIVIDE', 5, 0),/Cannot divide by zero/);
        });
        it('should return the quotient of the rounded numbers', function () {
            assert.notDeepEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2)
        });
        });

        describe('Invalid operation type', function () {
        it('should throw an error for an invalid operation type', function () {
            assert.throws(() => calculateNumber('Multiply', 4, 5), /Invalid operation type/);
        });
    });
});

function almostEqual(a, b, epsilon = 1e-9) {
    return Math.abs(a - b) < epsilon;
}
