const http = require('http');
const countStudents = require('./3-read_file_async');
// Retrieve the file path from the command-line arguments
const filePath = process.argv[2];

if (!filePath) {
    console.error('Usage: node 5-http.js <database.csv>');
    process.exit(1); // Exit if no file path is provided
}


// Create an HTTP server
const server = http.createServer(async (req, res) => {
    // Send a response depending on the URL
    if (req.url === '/') {
        // Set the response header
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Atlas School!');
    } else if (req.url === '/students') {
        try {
            // Capture the output from console.log
            let output = '';
            const originalConsoleLog = console.log;

            // Override console.log to capture the output in a string
            console.log = (message) => {
                output += message + '\n';
            };

            // Call countStudents (which uses console.log internally)
            await countStudents('database.csv');

            // Restore the original console.log
            console.log = originalConsoleLog;

            // Add a header message and send the response
            const responseText = `This is the list of our students\n${output}`;
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(responseText);
        } catch (err) {
            // Restore the original console.log on error
            console.log = originalConsoleLog;
            // Handle errors that occur in countStudents
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end(`Error: ${err.message}`);
        }
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
    }
});

// Export the app (HTTP server)
// module.exports = app;
// Start the server on port 3000
server.listen(1245, () => {
    console.log('Server is running on http://localhost:1245');
});
