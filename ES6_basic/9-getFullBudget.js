export default function getFullBudgetObject(income, gdp, capita) {
  const budget = {income, gdp, capita};
  const fullBudget = {
    ...budget,
    getIncomeInDollars: (income) => {
      return `$${income}`;
    },
    getIncomeInEuros: (income) => {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
