export default function appendToEachArrayValue(array, appendString) {
  for (var idx of array) {
    array[idx] = appendString + array[idx];
  }
  return array;
}
