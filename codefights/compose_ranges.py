from sgk_test import test
def composeRanges(nums):
    _len = len(nums)
    if _len == 0:
        return []
    retval = []
    i = 0   #i: 1
    s = str(nums[0])    #s: 0
    while i < _len:
        if i < _len-1 and nums[i+1]-1 == nums[i]:
            if s.endswith("->") == False:
                s += "->"
        else:
            if s.endswith("->"):
                s += str(nums[i])
            retval.append(s)
            if i < _len-1:
                s = str(nums[i+1])
        i +=1

    return retval



def main():
    ######### TESTS ############
    test(["-1->2", "6->7", "9"], composeRanges([-1, 0, 1, 2, 6, 7, 9]))
    test([], composeRanges([]))
    test(["-1"], composeRanges([-1]))
    test(["0->2", "4->5", "7"], composeRanges([0, 1, 2, 4, 5, 7]))

    test(["0->1"], composeRanges([0, 1])) # 6
    test(["1", "3"], composeRanges([1, 3])) # 8
    test(["0", "5", "9"], composeRanges([0, 5, 9])) # 11

if __name__ == "__main__":
    main()

