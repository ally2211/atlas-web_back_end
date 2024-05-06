
export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const locationStudents = students.filter((student) => student.location === city);

  const updatedStudents = locationStudents.map(student => {
    const matchingId = newGrades.find(grade => grade.id === student.id);
    if (matchingId) {
      return { ...student, grade: matchingId.grade };
    }
    else return { ...student, grade: 'N/A' };
    });

    console.log('Students:', students);
    console.log('New Grades:', newGrades);
    console.log('Updated Students:', updatedStudents);
  
}
