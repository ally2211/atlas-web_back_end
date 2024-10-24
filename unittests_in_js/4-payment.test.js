const sinon = require('sinon');
const { expect } = require('chai');
const calculateNumber = require('./utils.js'); // Import the original function
const sendPaymentRequestToApi = require('./4-payment.js'); // Import the function to test

describe('sendPaymentRequestToApi', () => {
    let consoleLogStub;
    let calculateNumberStub;

    beforeEach(() => {
        // Stub the calculateNumber function to always return 10
        calculateNumberStub = sinon.stub(calculateNumber, 'calculateNumber').returns(10);

        // Stub console.log
        consoleLogStub = sinon.stub(console, 'log');
    });

    afterEach(() => {
        // Restore the original functions
        calculateNumberStub.restore();
        consoleLogStub.restore();
    });

    it('should call calculateNumber with correct parameters and log the correct message', () => {
        sendPaymentRequestToApi(100, 20); // Call the function

        // Verify that the stub was called with the correct arguments
        expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;

        // Verify that console.log was called with the correct message
        expect(consoleLogStub.calledWith('The total is: 10')).to.be.true;
    });
});
