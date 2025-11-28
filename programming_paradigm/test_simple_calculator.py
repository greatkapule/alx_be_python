import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)
        self.assertEqual(self.calc.add(7, 0), 7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(7, 1), 7)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_consistency_with_python_ops(self):
        inputs = [ (2,3), (-1,4), (0,5), (5,2) ]
        for a, b in inputs:
            self.assertEqual(self.calc.add(a, b), a + b)
            self.assertEqual(self.calc.subtract(a, b), a - b)
            self.assertEqual(self.calc.multiply(a, b), a * b)
            if b != 0:
                self.assertEqual(self.calc.divide(a, b), a / b)

if __name__ == '__main__':
    unittest.main()
