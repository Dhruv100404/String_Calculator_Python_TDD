import unittest
from String_Calc import Calculator

class TestCalculator(unittest.TestCase):

    def test_should_return_zero_on_empty_string(self):
        self.assertEqual(Calculator.add(""), 0)

    def test_should_return_number_on_single_string(self):
        self.assertEqual(Calculator.add("1"), 1)

    def test_should_return_sum_of_numbers_on_two_strings(self):
        self.assertEqual(Calculator.add("1,2"), 3)

if __name__ == '__main__':
    unittest.main()
