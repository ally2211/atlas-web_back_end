const express = require('express');
const countStudents = require('./3-read_file_async');
const app = express();
// Retrieve the file path from the command-line arguments
const filePath = process.argv[2];

if (!filePath) {
    console.error('Usage: node 5-http.js <database.csv>');
    process.exit(1); // Exit if no file path is provided
}

app.get('/', (req, res) => {
    res.send('Hello Atlas School!');
});

// Handle the /students route

// Handle the /students route
app.get('/students', async (req, res) => {
    try {
        // Capture the output from console.log
        let output = 'This is the list of our students\n';
        const originalConsoleLog = console.log;

        // Override console.log to capture the output into the "output" string
        console.log = (message) => {
            output += message + '\n';
        };

        // Call countStudents (which uses console.log internally)
        await countStudents(filePath);

        // Restore the original console.log after capturing the output
        console.log = originalConsoleLog;

        // Send the captured output as the HTTP response
        res.status(200).send(output);
    } catch (error) {
        // Restore console.log on error and handle the case where the database cannot be loaded
        console.log = originalConsoleLog;
        res.status(500).send('This is the list of our students\nCannot load the database');
    }
});

app.listen(1245, () => {
    console.log('Express server running at http://localhost:1245/');
});
