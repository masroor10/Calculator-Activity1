import unittest
from division import divide_numbers

class TestDivision(unittest.TestCase):
    def test_positive_numbers(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = divide_numbers(-15, -3)
        self.assertEqual(result, 5)

    def test_mixed_numbers(self):
        result = divide_numbers(20, -5)
        self.assertEqual(result, -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()
