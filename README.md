# String Calculator

A simple string calculator that can handle addition of numbers provided in a string format. The calculator supports multiple delimiters including custom ones and handles edge cases such as empty input and negative numbers.

## Features

- Add numbers separated by commas.
- Handle newlines as delimiters.
- Support custom single-character delimiters.
- Throw exceptions for negative numbers, displaying the negative numbers in the exception message.

## Getting Started

### Prerequisites

- Python 3.x
- `unittest` library (comes with Python standard library)

## Usage
### To use the Calculator class in your own projects, import it and call the add method:

```python
from String_Calc import Calculator

result = Calculator.add("1,2,3")
print(result)  # Output: 6
```

## Running Tests

The project includes a suite of unit tests to ensure the calculator works correctly. To run the tests, use the following command:

```sh
python -m unittest .\String_Test.py
