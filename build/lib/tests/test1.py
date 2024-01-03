# Test case2: Importing  mod2 module
import sys
sys.path.append("C:\\Users\\cstech_\\mypkg")

from mypkg.mod2 import sqr, add, divs

import unittest

class TestMyFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(5, 3)
        self.assertEqual(result, 8, "Addition of positive numbers failed")

    def test_add_negative_numbers(self):
        result = add(-5, 3)
        self.assertEqual(result, -2, "Addition of negative and positive numbers failed")

    def test_sqr_positive_number(self):
        result = sqr(4)
        self.assertEqual(result, 16, "Square of a positive number failed")

    def test_sqr_negative_number(self):
        result = sqr(-3)
        self.assertEqual(result, 9, "Square of a negative number failed")

    def test_divs_integer_division(self):
        result = divs(10, 2)
        self.assertEqual(result, 5, "Integer division failed")

    def test_divs_float_division(self):
        result = divs(7, 3)
        self.assertAlmostEqual(result, 2.333, places=3, msg="Float division failed")

    def test_divs_divide_by_zero(self):
        # with self.assertRaises(ZeroDivisionError):
        divs(5, 0)
        
    def test_valid_division(self):
        result = divs(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
    
