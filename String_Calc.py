import re

class Calculator:
    @staticmethod
    def add(numbers):
        num = Calculator.splitter(numbers)
        return Calculator.find_sum(num)

    @staticmethod
    def find_sum(num):
        return sum(Calculator.to_int(n) for n in num)

    @staticmethod
    def splitter(numbers):
        if not numbers:
            return []
        elif Calculator.is_custom_delimiter_string(numbers):
            return Calculator.split_using_custom_delimiter(numbers)
        return Calculator.split_using_comma_and_new_line(numbers)

    @staticmethod
    def is_custom_delimiter_string(numbers):
        return numbers.startswith("//")

    @staticmethod
    def split_using_custom_delimiter(numbers):
        m = re.match("//(.)\n(.*)", numbers)
        custom_delim = m.group(1)
        num = m.group(2)
        return re.split(re.escape(custom_delim), num)

    @staticmethod
    def split_using_comma_and_new_line(numbers):
        return re.split(",|\n", numbers)

    @staticmethod
    def to_int(number):
        return int(number)
