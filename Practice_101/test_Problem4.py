import unittest
from Calc import *
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(Multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(Divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()