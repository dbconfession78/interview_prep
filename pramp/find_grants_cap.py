"""
Award Budget Cuts

The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget
allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However,
due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The
committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on
all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal
to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that
finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget
constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double
"""
from sgk_test import test
# def find_grants_cap_PRACTICE(grantsArray, newBudget):
def find_grants_cap(grantsArray, newBudget): # [210,200,150,193,130,110,209,342,117], 1530
    return


def find_grants_cap_SOL(grantsArray, newBudget):
# def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort()
    i = 0
    _len = len(grantsArray)
    while i < _len and grantsArray[i] < float(newBudget) / (_len - i):
        newBudget -= grantsArray[i]
        i += 1
    return newBudget / (_len - i)




def main():
    ######### TESTS ############
    test(47.0, find_grants_cap([2, 100, 50, 120, 1000], 190))
    test(1.5, find_grants_cap([2,4], 3))
    test(1.0, find_grants_cap([2,4,6], 3))
    test(128.0, find_grants_cap([2,100,50,120,167], 400))
    test(47.0, find_grants_cap([2,100,50,120,1000], 190))
    test(23.8, find_grants_cap([21,100,50,120,130,110], 140))
    test(211.0, find_grants_cap([210,200,150,193,130,110,209,342,117], 1530))


if __name__ == "__main__":
    main()

