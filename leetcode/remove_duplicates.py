from itertools import combinations
from random import random

def main():
    nums = [1, 1, 2]
    print(remove_duplicates(nums))


def remove_duplicates2(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
        return len(nums)

def remove_duplicates(nums):
    if (len(nums) == 0):
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1





if __name__ == '__main__':
    main()
