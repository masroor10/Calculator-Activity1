import unittest
from mul import mul_numbers

class TestMultiplicationFunction(unittest.TestCase):
    def test_positive_numbers(self):
        result = mul_numbers(5, 7)
        self.assertEqual(result, 35)

    def test_negative_numbers(self):
        result = mul_numbers(-5, -3)
        self.assertEqual(result, 15)

    def test_mixed_numbers(self):
        result = mul_numbers(10, -3)
        self.assertEqual(result, -30)

if __name__ == '__main__':
    unittest.main()