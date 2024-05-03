export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  // Explicitly check if expansion1989 and expansion2019 are undefined
  const isExpansion1989Undefined = expansion1989 === undefined;
  const isExpansion2019Undefined = expansion2019 === undefined;

  // Use the check results to determine the values to use
  const expansion1989Value = isExpansion1989Undefined ? 89 : expansion1989;
  const expansion2019Value = isExpansion2019Undefined ? 19 : expansion2019;

  return initialNumber + expansion1989Value + expansion2019Value;
}
