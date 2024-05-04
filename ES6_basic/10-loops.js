export default function appendToEachArrayValue(array, appendString) {
  let newArray = [];
  for (const value of array) {
    newArray.push(appendString + value); // Appends ' fruit' to each element
}
  return newArray;
}
