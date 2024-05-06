export default function cleanSet(newSet, startString) {
  const modifiedElements = [];
  
  if (startString === '') {
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
