export default function updateUniqueItems(itemMap) {
  for (let [key, value] of itemMap) {
    if (value === 1) {
      // Update the value to 100
      itemMap.set(key, 100);
    }
  }
  return itemMap;
}  
