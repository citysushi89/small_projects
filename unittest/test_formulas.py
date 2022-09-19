from re import L
import unittest 
from formulas import add, subtract, divide, multiply

# TODO add 2ish failures for each failure

# To Run:
    # python -m unittest test_formulas.py
    # python -m unittest -v test_formulas.py

class TestAdd(unittest.TestCase):
    # Test the function of add from formulas.py 

    def test_add_int(self):
        self.assertEqual(add(2, 2), 4)

    def test_add_float(self):
        self.assertEqual(add(2.04, 5.07), 7.11)

    def test_add_one_negative(self):
        self.assertEqual(add(2, -2), 0)

    def test_add_two_negative(self):
        self.assertEqual(add(-2, -3), -5)


class SubtractTest(unittest.TestCase):
    # Test the function of subtract from formulas.py 
    
    def test_subtract_int(self):
        self.assertEqual(subtract(2, 2), 0)

    # Use almost equal, below returns: AssertionError: 2.0200000000000005 != 2.02
    def test_subtract_float(self):
        self.assertAlmostEqual(subtract(4.03, 2.01), 2.02)

    def test_subtract_one_negative(self):
        self.assertEqual(subtract(5, -2), 7)

    def test_subtract_two_negative(self):
        self.assertEqual(subtract(-8, -4), -4)


class TestDivide(unittest.TestCase):
    # Test the function of divide from formulas.py 

    def test_divide_int(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_float(self):
        self.assertEqual(divide(10.5, 5.25), 2)

    def test_divide_one_negative(self):
        self.assertEqual(divide(4, -2), -2)

    def test_divide_two_negative(self):
        self.assertEqual(divide(-8, -2), 4)


class TestMultiply(unittest.TestCase):
    # Test the function of divide from formulas.py
    
    def test_multiply_int(self):
        self.assertEqual(multiply(4, 2), 8)

    def test_multiply_float(self):
        self.assertEqual(multiply(4.5, 2.25), 10.125)

    def test_multiply_one_negative(self):
        self.assertEqual(multiply(4, -2), -8)

    def test_multiply_two_negative(self):
        self.assertEqual(multiply(-5, -2), 10)
