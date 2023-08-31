import unittest
from add import add_numbers

class TestAdditionFunction(unittest.TestCase):
    def test_positive_numbers(self):
        result = add_numbers(5, 7)
        self.assertEqual(result, 12)

    def test_negative_numbers(self):
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)

    def test_mixed_numbers(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
