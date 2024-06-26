export default function getListStudents() {
  const studentArray = [{ id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];

  const updatedStudentArray = studentArray.map((student) => ({ ...student }));

  return updatedStudentArray;
}
