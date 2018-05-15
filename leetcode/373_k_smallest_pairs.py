# Instructions
"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        n1 = len(nums1)
        n2 = len(nums2)
        idx2 = [0 for x in range(n1)]
        retlst = []
        if n1 == 0 or n2 == 0:
            return []
        while k > 0:
            min_sum = float('inf')
            min_idx = 0

            for i1 in range(n1):
                i2 = idx2[i1]
                if i2 < n2 and nums1[i1] + nums2[i2] < min_sum:
                    min_idx = i1
                    min_sum = nums1[i1] + nums2[i2]

            if min_idx < n1 and idx2[min_idx] < n2:
                retlst.append([nums1[min_idx], nums2[idx2[min_idx]]])
            idx2[min_idx] += 1
            k -= 1

        return retlst


def main():
    print(Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3))

    print(Solution().kSmallestPairs(
        [41, 80, 106, 123, 128, 133, 146, 149, 157, 166],
        [29, 57, 79, 86, 88, 156, 168, 178, 179, 193],
        5))

    print(Solution().kSmallestPairs(
        [41, 80, 106, 123, 128, 133, 146, 149, 157, 166],
        [29, 57, 79, 86, 88, 156, 168, 178, 179, 193],
        7))

    print(Solution().kSmallestPairs([8,10,11,12,13], [3,4,5,6,7,19,20], 6))
    print(Solution().kSmallestPairs([], [], 5))
    print(Solution().kSmallestPairs([3,5,7,9], [], 1))
    print(Solution().kSmallestPairs([1,1,2], [1,2,3], 10))
    print(Solution().kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20))

#LC input
# [1,7,11]
# [2,4,6]
# 3
# [41, 80, 106, 123, 128, 133, 146, 149, 157, 166]
# [29, 57, 79, 86, 88, 156, 168, 178, 179, 193]
# 5
# [41, 80, 106, 123, 128, 133, 146, 149, 157, 166]
# [29, 57, 79, 86, 88, 156, 168, 178, 179, 193]
# 7
# [8,10,11,12,13]
# [3,4,5,6,7,19,20]
# 6
# []
# []
# 5
# [3,5,7,9]
# []
# 1
# [1,1,2]
# [1,2,3]
# 10
# [1,2,4,5,6]
# [3,5,7,9]
# 20


if __name__ == '__main__':
    main()
