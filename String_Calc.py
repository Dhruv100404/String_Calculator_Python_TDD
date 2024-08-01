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
        return re.split(",|\n", numbers)

    @staticmethod
    def to_int(number):
        return int(number)
