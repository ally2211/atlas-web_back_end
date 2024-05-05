export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const totalIdSum = students.reduce((accumulator, student) => accumulator + student.id, 0);

  return totalIdSum;
}
