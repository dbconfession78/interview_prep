"""
You are given an array of n integers, and a positive integer, k. Find and print the number of pairs where i < j and  a[i]+a[j]  is divisible by k.
"""
def divisibleSumPairs(k, ar):
    i = 0
    retval = 0
    _len = len(ar)

    ar.sort()
    print(ar)
    while i < _len:
        j = i + 1
        while j < _len:
            if (ar[i] + ar[j]) % k == 0:
                retval += 1
            j += 1
        i += 1
    return retval



# print(divisibleSumPairs(3, [1,3,2,6,1,2]))
# print(divisibleSumPairs(3, [1]))

input = '71 44 2 93 66 27 41 99 49 68 60 16 45 21 71 96 89 91 60 21 43 9 56 48 25 96 91 99 73 22 48 32 27 71 72 90 9 62 68 70 77 98 2 32 69 51 99 35 47 83 82 43 87 47 40 54 53 85 78 31 98 26 56 100 88 43 77 81 58 31 46 70 57 8 16 53 8 61 22 62 75 94 91 29 95 69 22 12 88 5 87 90 10 86 86 85 73 95 87 53'
input = [int(x) for x in input.split(' ')]
print(divisibleSumPairs(22, input))  # 182
