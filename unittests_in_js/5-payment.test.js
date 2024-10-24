const sinon = require('sinon');
const { expect } = require('chai');
const utils = require('./utils.js'); // Import the original function
const sendPaymentRequestToApi = require('./5-payment.js'); // Import the function to test

describe('sendPaymentRequestToApi', () => {
    let consoleLogStub;

    beforeEach(() => {
        // Stub console.log
        consoleLogStub = sinon.stub(console, 'log');
    });

    afterEach(() => {
        // Restore the original console.log
        consoleLogStub.restore();
    });

    it('should log the correct total for inputs 100 and 20', () => {
        // Call the function with specified inputs
        sendPaymentRequestToApi(100, 20);

        // Verify that console.log is called with the correct message
        expect(consoleLogStub.calledWith('The total is: 120')).to.be.true;

        // Verify that console.log was called only once
        expect(consoleLogStub.callCount).to.equal(1);
    });

    it('should log the correct total for inputs 10 and 10', () => {
        // Call the function with specified inputs
        sendPaymentRequestToApi(10, 10);

        // Verify that console.log is called with the correct message
        expect(consoleLogStub.calledWith('The total is: 20')).to.be.true;

        // Verify that console.log was called only once
        expect(consoleLogStub.callCount).to.equal(1);
    });
});

