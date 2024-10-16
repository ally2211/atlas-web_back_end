const express = require('express');
const router = require('./routes/index');


const app = express();
const port = 1245;
const filePath = process.argv[2];

if (!filePath) {
    console.error('Usage: node app.js <database.csv>');
    process.exit(1);
}

// Store the file path in app.locals for access within controllers
app.locals.filePath = filePath;

// Use the router defined in full_server/routes/index.js
app.use('/', router);

// Start the Express server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
