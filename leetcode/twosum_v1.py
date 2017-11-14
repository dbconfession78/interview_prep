#!/usr/bin/python3
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, first in enumerate(nums):
            second = target - first
            if second in nums[i+1:]:
                i2 = nums[i+1:].index(second) + i + 1
                return [i, i2]

def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    if not len_of_list:
        return "[]"

    result = ""
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
