import unittest
from String_Calc import Calculator

class TestCalculator(unittest.TestCase):

    def test_should_return_zero_on_empty_string(self):
        self.assertEqual(Calculator.add(""), 0)

    def test_should_return_number_on_single_string(self):
        self.assertEqual(Calculator.add("1"), 1)

    def test_should_return_sum_of_numbers_on_two_strings(self):
        self.assertEqual(Calculator.add("1,2"), 3)

    def test_should_return_sum_of_all_numbers(self):
        self.assertEqual(Calculator.add("1,2,3"), 6)

    def test_should_allow_new_line_as_delimiter(self):
        self.assertEqual(Calculator.add("1\n2,3"), 6)

    def test_should_allow_custom_delimiter(self):
        self.assertEqual(Calculator.add("//;\n1;2"), 3)

    def test_should_allow_regex_char_as_custom_delimiter(self):
        self.assertEqual(Calculator.add("//.\n1.2"), 3)

if __name__ == '__main__':
    unittest.main()
