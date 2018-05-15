"""
How many ways can you make the sum of a number?

From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples

Trivial

sum(-1) # 0
sum(1) # 1
Basic

sum(2) # 2  -> 1+1 , 2
sum(3) # 3 -> 1+1+1, 1+2, 3
sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

sum(10) # 42
Explosive

sum(50) # 204226
sum(80) # 15796476
sum(100) # 190569292
"""
class Solution():
    def exp_sum(self, n):

        def helper(lst, i, num,  reduced_num):
            if reduced_num < 0:
                return
            if reduced_num == 0:
                i = 0
                while i < i:

                    i += 1
            lst = []
            if n == 0:
                return retval
            elif n >= 0:
                k = 1
                while k <= MAX:
                    lst.append(k)
                    helper(n-k, i+1, retval)
                    k += 1
            return retval

        lst = [None for _ in range(n)]
        return helper(lst, 0, n, n)



def main():
    print(Solution().exp_sum(4))  # 5
    print(Solution().exp_sum(3))  # 2


if __name__ == '__main__':
    main()
