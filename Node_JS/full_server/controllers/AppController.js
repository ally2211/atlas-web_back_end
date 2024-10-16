// Controllers/AppController.js
const readDatabase = require('../utils');


// Controller methods
class AppController {
    static getHomepage(req, res) {
        res.status(200).send('Hello Atlas School!');
    }
}

module.exports = AppController;
//module.exports = StudentsController;
