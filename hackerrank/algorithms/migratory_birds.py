"""
A flock of n birds is flying across the continent. Each bird has a type, and the different types are designated by the ID numbers 1, 2, 3, 4, and 5.

Given an array of n integers where each integer describes the type of a bird in the flock, find and print the type number of the most common bird. If two or more types of birds are equally common, choose the type with the smallest ID number.
"""
from collections import defaultdict
def migratoryBirds(n, ar):
    retval = None
    _max = 0
    dct = defaultdict(int)
    for bird in ar:
        dct[bird] += 1
        if retval is None:
            retval = bird
            _max = 1
        else:
            if dct[bird] == _max:
                retval = min(retval, bird)
            if dct[bird] > _max:
                retval = bird
                _max = dct[bird]
    return retval



print(migratoryBirds(6, [1,4,4,4,5,3]))
print(migratoryBirds(8, [1,3,4,4,4,5,5,5]))


input = '7'
input = [int(x) for x in input.split(' ')]

