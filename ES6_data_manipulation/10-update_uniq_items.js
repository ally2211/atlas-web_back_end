export default function updateUniqueItems(itemMap) {
  // Check if the argument is a Map
  if (!(itemMap instanceof Map)) {
    // Throw an error if the argument is not a Map
    throw new Error('Cannot process: argument is not a Map');
  }
  for (const [key, value] of itemMap) {
    if (value === 1) {
      // Update the value to 100
      itemMap.set(key, 100);
    }
  }
  return itemMap;
}
