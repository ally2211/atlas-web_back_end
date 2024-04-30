export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    let task = true;  // Update the variable without redeclaring it
    let task2 = false;  // Update the variable without redeclaring it
  }

  return [task, task2];
}
