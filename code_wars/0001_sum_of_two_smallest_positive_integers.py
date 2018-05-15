"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

Hint: Do not modify the original array.
"""

class Solution():
    def sum_two_smallest_numbers(self, numbers):
        numbers.sort()
        _len = len(numbers)
        i = 0
        while i < _len and numbers[i] < 1:
            i += 1

        if i < _len - 1:
            return numbers[i] + numbers[i + 1]

def main():
    print(Solution().sum_two_smallest_numbers([19, 5, 42, 2, 77]))      # 7
    print(Solution().sum_two_smallest_numbers([-19, 5, 42, 2, 77]))     # 7


if __name__ == '__main__':
    main()