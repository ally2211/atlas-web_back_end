const fs = require('fs');

// Function to count students and list their names by group
function countStudents(filePath) {
    try {
        // Read the CSV file synchronously
        const data = fs.readFileSync(filePath, 'utf8');
        
        // Split the file content by newlines to get rows
        const lines = data.split('\n');
        
        // Assuming the first line is the header
        const header = lines[0].split(',');
        const firstnameIndex = header.indexOf('firstname');
        const groupnameIndex = header.indexOf('field');
        
        if (firstnameIndex === -1 || groupnameIndex === -1) {
            throw new Error("CSV file must contain 'firstname' and 'field' columns.");
        }

        // Object to store grouped names
        const groups = {};

        // Iterate over each line (starting from line 1, which is after the header)
        for (let i = 1; i < lines.length; i++) {
            const line = lines[i].trim();
            if (line === '') continue;  // Skip empty lines

            const row = line.split(',');

            const firstname = row[firstnameIndex].trim();
            const groupname = row[groupnameIndex].trim();

            // Add the firstname to the appropriate group
            if (!groups[groupname]) {
                groups[groupname] = [];
            }
            groups[groupname].push(firstname);
        }

        // Print the output as required
        for (const [group, names] of Object.entries(groups)) {
            const numStudents = names.length;
            const nameList = names.join(', ');
            console.log(`Number of students in ${group}: ${numStudents}. List: ${nameList}`);
        }

    } catch (err) {
        console.error(`Error processing file: ${err.message}`);
        console.error(`Error: Cannot load the database`);
    }
}

// Export the function
module.exports = countStudents;