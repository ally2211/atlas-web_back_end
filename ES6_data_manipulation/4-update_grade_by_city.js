export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const locationStudents = students.filter((student) => student.location === city);

  const updatedStudents = locationStudents.map(student => {
    const matchingId = newGrades.find(grade => grade.id === student.id);
    if (matchingId) {
      updatedStudents = { ...student, grade: matchingId.grade };
      console.log(matchingId.grade);
    }
    else return { ...student, grade: 'N/A' };
  });
  return updatedStudents;
}
