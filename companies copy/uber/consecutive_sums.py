# Instructions
"""
Count number of possible consecutive sums that add up to 'num'

e.g.
input : num = 15
Output: 3

Explanation:
sum1: 1+2+3+4+5=15
sum2: 4+5+6
sum3: 7+8

Since there are 3 sums that add to 15, the output is 3
"""
def consecutive(num):
    i = 1
    j = num
    count = 0
    _sum = sum([x for x in range(1, num+1)])
    while i < j and j <= num:
        if _sum > num:
            _sum -= j
            j -= 1
        elif _sum < num:
            _sum -= i
            i += 1
            j += 1
            _sum += j
        else:
            count += 1
            j += 1
            _sum += (j-i)
            i += 1
    return count


def main():
    print(consecutive(15))      # 3
    print(consecutive(2))       # 0
    print(consecutive(1))       # 0
    print(consecutive(10))      # 1
    print(consecutive(0))       # 0
    print(consecutive(100))     # 2
    print(consecutive(125))     # 3


if __name__ == '__main__':
    main()


"""
--


def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
