import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (-2, -3, -5)
        ]
        for value1, value2, expected in test_cases:
            with self.subTest(value1=value1, value2=value2):
                self.assertEqual(self.calculator.add(value1, value2), expected)

    def test_divide(self):
        test_cases = [
            (6, 2, 3),
            (6, -2, -3),
            (-6, -2, 3),
            (1, 0, ValueError)  # Special case for division by zero
        ]
        for dividend, divisor, expected in test_cases:
            if expected is ValueError:
                with self.assertRaises(ValueError) as context:
                    self.calculator.divide(dividend, divisor)
                self.assertEqual(str(context.exception), "Cannot divide by zero")
            else:
                with self.subTest(dividend=dividend, divisor=divisor):
                    self.assertEqual(self.calculator.divide(dividend, divisor), expected)

if __name__ == '__main__':
    unittest.main()
