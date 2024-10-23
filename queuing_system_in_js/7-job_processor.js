const kue = require('kue');
const queue = kue.createQueue();



// Create an array to hold blacklisted phone numbers
const blacklistedNumbers = [];

// Add blacklisted phone numbers
blacklistedNumbers.push('4153518780');
blacklistedNumbers.push('4153518781');

// Alternatively, you can initialize the array with the numbers directly
// const blacklistedNumbers = ['4153518780', '4153518781'];

// Log the blacklisted numbers to verify
console.log('Blacklisted Phone Numbers:', blacklistedNumbers);



// Function to send a notification
function sendNotification(phoneNumber, message, job, done) {
    job.progress(0); //start at 0%

    //Check if the phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)){
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
        done(error);  //fail the job with an error
        return; // exit the function
    }

    // If not blacklisted, track the progress to 50%
    job.progress(50); // Update progress to 50%

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    done(null); // success
}



// Queue process to listen for new jobs on 'push_notification_code'
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function
    sendNotification(phoneNumber, message, {
        progress: (percentage) => {
            console.log(`Job ${job.id} progress: ${percentage}%`);
        }
    }, (error) => {
        if (error) {
            console.error(`Error processing job ${job.id}: ${error.message}`);
            done(error); // Fail the job
        } else {
            console.log(`Job ${job.id} processed successfully.`);
            done(); // Mark the job as done
        }
    });
});
