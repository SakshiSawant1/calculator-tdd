class StringCalculator:
    """
    A class to calculate the sum of numbers from a given string.
    Supports custom delimiters and handles various input formats.
    """
    def __init__(self):
        self.delimiter = ','
    def add(self, numbers: str) -> int:
        #for string is empty Return 0 if
        if not numbers:
            return 0
