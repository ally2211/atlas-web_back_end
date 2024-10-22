const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

// Function to create a job
function createNotificationJob(notificationData) {
    // Create a job in the push_notification_code queue
    const job = queue.create('push_notification_code', notificationData)
        .save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            } else {
                console.log('Error creating job:', err);
            }
        });

    // Event listener for job completion
    job.on('complete', () => {
        console.log('Notification job completed');
    });

    // Event listener for job failure
    job.on('failed', () => {
        console.log('Notification job failed');
    });
}

// Example notification data
const notificationData = {
    phoneNumber: '1234567890',
    message: 'You have a new notification!'
};

// Create the job
createNotificationJob(notificationData);
