// Controllers/AppController.js
const readDatabase = require('../utils');

// Controller methods
class StudentsController {
    static async getAllStudents(req, res) {
        const { filePath } = req.app.locals;
        try {
            const students = await readDatabase(filePath);
            let responseText = 'This is the list of our students\n';

            // Format the output
            for (const [major, names] of Object.entries(students)) {
                responseText += `Number of students in ${major}: ${names.length}. List: ${names.join(', ')}\n`;
            }

            res.status(200).send(responseText);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const { filePath } = req.app.locals;
        const { major } = req.params;

        try {
            const students = await readDatabase(filePath);

            if (!students[major]) {
                return res.status(500).send(`Major parameter must be CS or SWE`);
            }

            const list = students[major].join(', ');
            res.status(200).send(`List: ${list}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

module.exports = StudentsController;
