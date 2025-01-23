import pytest
from stringsum_tdd import StringCalculator

class TestStringCalculator:
     # For empty string
    def test_empty_string(self):
        calc = StringCalculator()
        assert calc.add("") == 0
    # For custom delimiter
    def test_custom_delimiter(self):
        calc = StringCalculator()
        assert calc.add("//;\n1;2") == 3
    # For a single number
    def test_single_number(self):
        calc = StringCalculator()
        assert calc.add("1") == 1
    