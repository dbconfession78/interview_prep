# Instructions
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
class Solution:
    # def trap_PRACTICE(self, height):
    def trap(self, height):
        i = 0
        vol = 0
        i = 0
        stk = [] # todo account for idx 0 having val higher than 0
        while i < len(height):
            _this = height[i]
            while stk and _this > height[stk[-1]]:
                top = stk.pop()
                if not stk:
                    break
                lo = min(height[stk[-1]], _this) - height[top]
                dist = abs(i - stk[-1] - 1)
                vol += dist * lo
                # vol += (lo - height[stk.pop()]) - height[stk[-1]]
            stk.append(i)


            i += 1
        return vol

    def trap_BRUTE(self, height):
    # def trap(self, height):
        _len = len(height)
        i = 1
        retval = 0
        while i < _len - 1:
            max_left = 0
            max_right = 0
            j = i
            while j >= 0:
                max_left = max(max_left, height[j])
                j -= 1
            j = i
            while j < _len:
                max_right = max(max_right, height[j])
                j += 1
            retval += min(max_left, max_right) - height[i]
            i += 1
        return retval

    def trap_STACK(self, height):
    # def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        _len = len(height)
        vol = 0
        i = 0
        stk = []
        while i < _len:
            while stk and height[i] > height[stk[-1]]:
                top = stk[-1]
                stk.pop()
                if stk == []:
                    break
                dist = i - stk[-1] - 1
                bound_height = min(height[i], height[stk[-1]]) - height[top]
                vol += dist * bound_height

            stk.append(i)
            i += 1
        return vol




def main():
    # print(Solution().trap([]))                          # 0
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
    # print(Solution().trap([2,0,2]))                     # 2
    # print(Solution().trap([4,2,3]))                     # 1
    # print(Solution().trap([4,1,0,2,1,0,1,3,2,1,2,1]))     #14

#LC Input
# []
# [0,1,0,2,1,0,1,3,2,1,2,1]
# [2,0,2]
# [4,2,3]
if __name__ == '__main__':
    main()