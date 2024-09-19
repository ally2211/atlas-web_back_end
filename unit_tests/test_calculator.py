# test_calculator.py

import unittest
from calculator import Calculator  # Import the Calculator class



class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-2, -3), -5)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(6, -2), -3)
        self.assertEqual(self.calculator.divide(-6, -2), 3)
        
        with self.assertRaises(ValueError) as context:
            self.calculator.divide(1, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
