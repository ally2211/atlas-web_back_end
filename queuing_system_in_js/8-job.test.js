const kue = require('kue');
const { expect } = require('chai');
const createPushNotificationJobs = require('./8-job.js'); // Import the function

// Enable test mode for Kue
const queue = kue.createQueue();
queue.testMode.enter(); // Enter test mode

describe('createPushNotificationJobs', () => {
    afterEach(() => {
        // Clear the queue after each test
        queue.testMode.clear();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationJobs('not-an-array', queue)).to.throw('Jobs is not an array');
    });

  
});
