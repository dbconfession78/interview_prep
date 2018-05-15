"""
Giarr[m]en a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The arr[m]alue k is positiarr[m]e and will always be smaller than the length of the sorted array.
Length of the giarr[m]en array is positiarr[m]e and will not exceed 104
Absolute arr[m]alue of elements in the array and x will not exceed 104
"""


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[0:k]
        if x >= arr[-1]:
            return arr[len(arr)-k:len(arr)]

        left = 0
        right = len(arr)-1
        count = k
        
        while left <= right:
            m = (left+right) // 2
            if arr[m] == x:
                break
            if arr[m] > x:
                right = m - 1
            else:
                left = m + 1
        m = (left+right) // 2
        retlst = [arr[m]]
        count -= 1

        left_lst = []
        right_lst = []
        left = m - 1
        right = m + 1
        while count > 0:
            if left >= 0:
                if right < len(arr):
                    l_diff = abs(x-arr[left])
                    r_diff = abs(x-arr[right])
                    if l_diff <= r_diff:
                        left_lst.insert(0, arr[left])
                        left -= 1
                        count -= 1
                    else:
                        right_lst.append(arr[right])
                        right += 1
                        count -= 1
                else:
                    left_lst.insert(0, arr[left])
                    left -= 1
                    count -= 1
            elif right < len(arr):
                right_lst.append(arr[right])
                right += 1
                count -= 1

            if count == 0:
                break

        return left_lst + retlst + right_lst


def main():
    print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))                # [1,2,3,4]
    print(Solution().findClosestElements([5, 6, 7, 8, 9], 4, 3))                # [5,6,7,8]
    print(Solution().findClosestElements([5, 6, 7, 8, 9], 4, 10))               # [6,7,8,9]
    print(Solution().findClosestElements([5, 6, 7, 8, 9, 10, 18, 22, 91], 4, 11))   # [7,8,9,10]
    print(Solution().findClosestElements([5, 6, 7, 8, 9, 10, 13, 22, 91], 4, 11))   # [8,9,10,13]


if __name__ == '__main__':
    main()
