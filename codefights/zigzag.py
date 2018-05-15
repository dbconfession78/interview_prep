class Solution:
    from collections import defaultdict
    def zigzag(self, nums):
        f = 0
        e = 0
        retval = 0
        while e < len(nums)-1:
            win = nums[f:e+1]
            retval = max(retval, len(win))
            if (nums[e] > nums[e-1] and nums[e] > nums[e+1]) or (nums[e] < nums[e-1] and nums[e] < nums[e+1]):
                # retval = max(retval, len(win))
                e += 1
            else:
                f += 1
                e = f + 1
        return retval


def main():
    print(Solution().zigzag([4, 2, 3, 1, 5, 3]))
    print(Solution().zigzag([7, 3, 5, 5, 2]))
    print(Solution().zigzag([3, 8, 6, 4, 5]))
    print(Solution().zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6]))    # 4


if __name__ == '__main__':
    main()
