export default function getListStudents() {
  const studentArray = [{ id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
  
// Function to format each student's information
function formatStudentInfo(student) {
 return `{ id: ${student.id}, firstName: ${student.firstName}, location: ${student.location} },`
 ;
}

// Iterate over studentArray and apply formatting to each student
const formattedStudents = studentArray.map(formatStudentInfo);

// Join the formatted strings into a single string
const allStudentsInfo = formattedStudents.join('\n  ');

 // Return the single string enclosed in square brackets
 return `[\n  ${allStudentsInfo}\n]`;
}
