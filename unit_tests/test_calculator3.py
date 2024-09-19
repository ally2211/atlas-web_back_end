import unittest
from parameterized import parameterized
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    @parameterized.expand([
        (2, 3, 5),
        (-1, 1, 0),
        (-2, -3, -5)
    ])
    def test_add(self, value1, value2, expected):
        self.assertEqual(self.calculator.add(value1, value2), expected)

    @parameterized.expand([
        (6, 2, 3),
        (6, -2, -3),
        (-6, -2, 3),
        (1, 0, ValueError)  # Special case for division by zero
    ])
    def test_divide(self, dividend, divisor, expected):
        if expected is ValueError:
            with self.assertRaises(ValueError) as context:
                self.calculator.divide(dividend, divisor)
            self.assertEqual(str(context.exception), "Cannot divide by zero")
        else:
            self.assertEqual(self.calculator.divide(dividend, divisor), expected)

if __name__ == '__main__':
    unittest.main()
