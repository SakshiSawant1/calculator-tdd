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
            # for a custom delimiter at the start
        nums = numbers
        if numbers.startswith('//'):
            delimiter, nums = numbers[2:].split('\n', 1)
            nums = nums.replace('\n', delimiter)
            nums = nums.replace(delimiter, ',')
