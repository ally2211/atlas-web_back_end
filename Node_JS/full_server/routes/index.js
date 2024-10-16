// full_server/routes/index.js

const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

// Link the route / to the AppController.getHomepage
router.get('/', AppController.getHomepage);

// Link the route /students to the AppController.getStudents
router.get('/students', StudentsController.getAllStudents);

// Link the route /students/:major to the AppController.getStudentsByMajor
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
