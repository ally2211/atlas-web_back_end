// test/rounding.test.js
//const assert = require('assert');
//const expect = require('chai');
import { expect } from 'chai';
//const calculateNumber = require('./2-calcul_chai.js');
import calculateNumber from './2-calcul_chai.js';

describe('calculateNumber', function () {
        describe('Sum operation', function () {
        it('should return the sum of the rounded numbers', function () {
            //assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6); // 5 + 5
            const result = calculateNumber('SUM', 1.4, 4.5)
            expect(result).to.equal(6); // 5 + 5
        });
        });

        describe('Subtract operation', function () {
        it('should return the difference of the rounded numbers', function () {
            // assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4); // 6 - 2
            const result = calculateNumber('SUBTRACT', 1.4, 4.5)
            expect(result).to.equal( -4); // 6 - 2
        });
        });

        describe('Divide operation', function () {
        it('should throw an error when dividing by zero', function () {
            //assert.throws(() => calculateNumber('DIVIDE', 5, 0),/Cannot divide by zero/);
            //const result = calculateNumber('DIVIDE', 5, 0)
            expect(() => calculateNumber('DIVIDE', 5, 0)).to.throw('Cannot divide by zero');

            //expect(result).to.equal(6); // 5 + 5
        });
        it('should return the quotient of the rounded numbers', function () {
            //assert.notDeepEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2)
            const result = calculateNumber('SUM', 1.4, 4.5)
            expect(result).to.equal(6); // 5 + 5
        });
        });

        describe('Invalid operation type', function () {
        it('should throw an error for an invalid operation type', function () {
            //assert.throws(() => calculateNumber('Multiply', 4, 5), /Invalid operation type/);
            expect(() => calculateNumber('invalid', 4, 5)).to.throw('Invalid operation type');
        });
    });
});
