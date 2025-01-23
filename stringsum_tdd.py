class StringCalculator: 
    def add(self, numbers: str) -> int:
        """
        Calculate the sum of numbers in the given string.

        Args:
            numbers (str): A string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers in the string.
        """
        # for  empty string retuen 0
        if not numbers:
            return 0
        # for string is custom delimiter at the start
        nums = numbers
        if numbers.startswith('//'):
            delimiter, nums = numbers[2:].split('\n', 1)
            # Use the custom delimiter 
            nums = nums.replace('\n', delimiter)
            nums = nums.replace(delimiter, ',')
        else:
            nums = nums.replace('\n', ',')
        # Split string and convert into integers
        integers = [int(n) for n in nums.split(',')]
        # Negative numbers are not allowed
        negatives = [n for n in integers if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
        # Return the sum of integers
        return sum(integers)
