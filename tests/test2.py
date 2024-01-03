
import sys
import os
sys.path.append(os.path.abspath('mypkg\..\..'))
from mypkg import mod1

from mypkg.mod1 import sub,func,funct
import unittest

print(funct([1,1,2,3,4,5]))
class TestMyFunctions(unittest.TestCase):

    def test_sub_positive_numbers(self):
        result = sub(5, 2)
        self.assertEqual(result, 3, "Subtraction of positive numbers failed")

    def test_sub_negative_numbers(self):
        result = sub(-5, -2)
        self.assertEqual(result, -3, "Subtraction of negative numbers failed")

    def test_sub_mixed_numbers(self):
        result = sub(5, -2)
        self.assertEqual(result, 7, "Subtraction of mixed numbers failed")



    def test_func_single_element_list(self):
        result = func([7,2])
        self.assertEqual(result, 1, "Function with a single-element list failed")
    def test_func_empty_list(self):
        result = func([])
        self.assertEqual(result, 0, "Function with an empty list failed")

    def test_func_multiple_element_list(self):
        result = func([3, 1, 2, 3, 1, 3])
        self.assertEqual(result, 2, "Function with multiple-element list failed")

if __name__ == '__main__':
    unittest.main()
