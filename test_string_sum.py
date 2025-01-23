import pytest
from stringsum_tdd import StringCalculator

class TestStringCalculator:
     # For empty string
    def test_empty_string(self):
        calc = StringCalculator()
        assert calc.add("") == 0
    
    