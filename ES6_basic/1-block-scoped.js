export default function taskBlock(trueOrFalse) {
    var task = false;
    var task2 = true;

    if (trueOrFalse) {
        var newtask = true;  // Update the variable without redeclaring it
        var newtask2 = false;  // Update the variable without redeclaring it
    }

    return [task, task2];
}
