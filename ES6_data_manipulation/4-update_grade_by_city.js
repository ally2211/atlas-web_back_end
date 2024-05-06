export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const locationStudents = students.filter((student) => student.location === city);

  return locationStudents.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
    return { ...student, grade: matchingGrade ? matchingGrade.grade : 'N/A' };
  });
}
