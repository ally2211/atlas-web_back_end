export default function hasValuesFromArray(newSet, newArray) {
  for (let i = 0; i < newArray.length; i++) {
    if (!newSet.has(newArray[i])) {
      return false; // If any element is not found in the set, return false
    }
  }
    return true; // If all elements are found in the set, return true
}
