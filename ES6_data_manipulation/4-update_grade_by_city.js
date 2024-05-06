export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const locationStudents = students.filter((student) => student.location === city);

  const updatedStudents = locationStudents.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (matchingGrade) {
      return { ...student, grade: matchingGrade.grade };
    }
    else {
      return { ...student, grade: 'N/A' };
    }
  });

  return updatedStudents;
}
