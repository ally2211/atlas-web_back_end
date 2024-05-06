export default function cleanSet(newSet, startString) {
  const modifiedElements = [];
  // Check if startString is not a string or is an empty string
  if (startString === '') {
    return '';
  }
  if (typeof startString !== 'string') {
    // Return an empty string if the condition is met
    throw new TypeError('startString must be a non-empty string');
  }
  newSet.forEach((element) => {
    if (element.startsWith(startString)) {
      const modifiedElement = element.replace(startString, '');
      modifiedElements.push(modifiedElement);
    }
  });
  return modifiedElements.join('-');
}
