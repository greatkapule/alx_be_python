import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (2.5, 0.5, 3.0),
            (-2.5, -1.5, -4.0),
            (10**6, 10**6, 2 * 10**6),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_subtraction(self):
        cases = [
            (5, 3, 2),
            (3, 5, -2),
            (0, 0, 0),
            (2.5, 0.5, 2.0),
            (-1, -1, 0),
            (10**6, 1, 10**6 - 1),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_multiplication(self):
        cases = [
            (2, 3, 6),
            (0, 100, 0),
            (-2, 3, -6),
            (2.5, 2, 5.0),
            (-1.5, -2, 3.0),
            (10**3, 10**3, 10**6),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_division_normal(self):
        cases = [
            (10, 2, 5.0),
            (3, 2, 1.5),
            (-6, 3, -2.0),
            (2.5, 0.5, 5.0),
            (0, 5, 0.0),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_non_numeric_inputs_raise(self):
        with self.assertRaises(TypeError):
            self.calc.add("a", 1)

        with self.assertRaises(TypeError):
            self.calc.subtract(1, "b")

        with self.assertRaises(TypeError):
            self.calc.multiply("x", "y")

        with self.assertRaises(TypeError):
            self.calc.divide("ten", 2)

if __name__ == "__main__":
    unittest.main()
