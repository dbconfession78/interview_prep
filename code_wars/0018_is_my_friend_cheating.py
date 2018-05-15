"""
A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (don't worry, n is always strictly greater than 0 and small enough so we shouldn't have overflow) and returns an array of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).

(See examples for each language in "RUN EXAMPLES")

#Examples:

removNb(26) should return [(15, 21), (21, 15)]
or

removNb(26) should return { {15, 21}, {21, 15} }
or

removeNb(26) should return [[15, 21], [21, 15]]
or

removNb(26) should return [ {15, 21}, {21, 15} ]
or

"""
from string import punctuation
class Solution():

    def removNb(self, n):
        MAX = 2 ** 31 - 1
        sum = (n * (n+1.0)) / 2.0
        retval = []
        b = n
        while b > 0:
            a = (sum - b) / (b + 1)
            int_a = int(a)
            if a < n and (a - int(a)) == 0:
                retval.append([int(a), int(b)])
            b -= 1
        return retval







def main():
    # print(Solution().removNb(100))   # []
    # print(Solution().removNb(26))   # [(15, 21), (21, 15)]
    # print(Solution().removNb(10))   #
    print(Solution().removNb(2147483646))  # []






if __name__ == '__main__':
    main()