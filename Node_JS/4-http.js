const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Set the response header
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    // Send a response depending on the URL
    if (req.url === '/') {
        res.end('Hello Atlas School!');
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
    }
});

// Start the server on port 3000
server.listen(1245, () => {
    console.log('Server is running on http://localhost:1245');
});
