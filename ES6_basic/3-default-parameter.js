export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {

  const expansion1989Value = expansion1989 === undefined ? 89 : expansion1989;
  const expansion2019Value = expansion2019 === undefined ? 19 : expansion2019;

  return initialNumber + expansion1989Value + expansion2019Value;
}