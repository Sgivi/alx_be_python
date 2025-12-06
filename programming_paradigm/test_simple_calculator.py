
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    # A SimpleCalculator object before each test.
    def setUp(self):
        self.calculator = SimpleCalculator()
        
    # Test addition
    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0, 5), 5)
        self.assertEqual(self.calculator.add(2.5, 3.5), 6.0)

    # Test subtraction
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(5.5, 2.5), 3.0)


    # Test multiplication
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(2.5, 4), 10.0)
        
    # Test division
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 2), -3)
        self.assertEqual(self.calculator.divide(-6, -2), 3)
        self.assertIsNone(self.calculator.divide(5, 0))  # Division by zero
        self.assertEqual(self.calculator.divide(7.5, 2.5), 3.0)
        
if __name__ == '__main__':
    unittest.main()