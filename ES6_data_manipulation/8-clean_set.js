export default function cleanSet(newSet, startString) {
  const modifiedElements = [];
  // Check if startString is not a string or is an empty string
  if (typeof startString === 'undefined' || startString === '') {
    return '';
  }
  if (typeof startString !== 'string') {
    return '';
  }
  newSet.forEach((element) => {
    if (element.startsWith(startString)) {
      const modifiedElement = element.replace(startString, '');
      modifiedElements.push(modifiedElement);
    }
  });
  return modifiedElements.join('-');
}
