const kue = require('kue');
const queue = kue.createQueue();

// Function to send a notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen for new jobs on 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function
    sendNotification(phoneNumber, message);

    // Mark the job as done
    done();
});

// Log errors if the queue encounters any
queue.on('error', (err) => {
    console.log('Queue error:', err);
});