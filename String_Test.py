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

    def test_should_throw_exception_for_negative_numbers(self):
        with self.assertRaises(RuntimeError):
            Calculator.add("1,-2,3")

    def test_should_have_negative_numbers_in_exception(self):
        with self.assertRaises(RuntimeError) as cm:
            Calculator.add("-1,-2,3")
        self.assertEqual(str(cm.exception), "negatives not allowed: -1, -2")

if __name__ == '__main__':
    unittest.main()
