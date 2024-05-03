export default function appendToEachArrayValue(array, appendString) {
  for (let element of array) {
    element = appendString + element;
  }
  return array;
}
