export default function hasValuesFromArray(newSet, newArray) {
  return newArray.every(element => newSet.has(element));
}
