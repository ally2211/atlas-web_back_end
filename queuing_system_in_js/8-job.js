const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

//import createPushNotificationsJobs from './8-job.js';


// Function to create a job for each notification
function createPushNotificationJobs(jobs, queue) {
    // Check if jobs is an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
            if (!err) {
            console.log(`Notification job created: ${job.id}`);
            } else {
            console.log('Error creating job:', err);
            }
        });

    // Event listener for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Event listener for job failure
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Event listener for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

// Create the jobs from the array
//createPushNotificationJobs(jobs, queue);

module.exports = createPushNotificationJobs; // Export the function