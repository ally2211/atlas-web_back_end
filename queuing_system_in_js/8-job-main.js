const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

//import createPushNotificationsJobs from './8-job.js';

const createPushNotificationJobs = require('./8-job.js'); // Import the function



const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];

createPushNotificationJobs(list, queue);

