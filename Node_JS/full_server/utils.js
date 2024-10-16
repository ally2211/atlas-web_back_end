// full_server/utils.js

const fs = require('fs').promises;

async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.trim().split('\n');

        if (lines.length === 0) {
            throw new Error('Cannot load the database');
        }

        // Parse the database file into a structure
        const students = {};
        lines.slice(1).forEach(line => {
            const [firstname, , , major] = line.split(',');
            if (!students[major]) {
                students[major] = [];
            }
            students[major].push(firstname);
        });

        return students;
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = readDatabase;
