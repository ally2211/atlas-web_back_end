export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const locationStudents = students.filter((student) => student.location === city);

  const updatedStudents = [];
  locationStudents.forEach((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
    updatedStudents.push({ ...student, grade: matchingGrade ? matchingGrade.grade : 'N/A' });
  });
  return updatedStudents;
}
