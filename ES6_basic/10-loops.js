export default function appendToEachArrayValue(array, appendString) {
  array.forEach((element, idx) => {
    array[idx] = appendString + element;
  });
  return array;
}
