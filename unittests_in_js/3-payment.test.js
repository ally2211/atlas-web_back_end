
const sinon = require('sinon'); // Import Sinon
//let { calculateNumber } = require('./utils.js'); // Import the function to spy on
const sendPaymentRequestToApi = require('./3-payment.js'); // Import the function to test



describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber with correct parameters', () => {
    spy = sinon.spy(calculateNumber);
    
    // Replace the original function with the spy
    const originalCalculateNumber = calculateNumber;
    const calculateNumber = spy;

    // Call the function under test
    sendPaymentRequestToApi(100, 20);
    // Assertions
    sinon.assert.calledOnce(spy); // Check if it was called once
    sinon.assert.calledWith(spy, 'SUM', 100, 20); // Check if it was called with the correct arguments

    // Restore the original function
    calculateNumber = originalCalculateNumber;
  });
});