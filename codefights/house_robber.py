from sgk_test import test, test_no
def house_robber(nums):
    prev_max = 0
    curr_max = 0
    _len = len(nums)
    for i in range(_len):
        tmp = curr_max
        curr_max = max(curr_max, prev_max + nums[i])
        prev_max = tmp
    return curr_max


def main():
    ######### TESTS ############
    test(2, house_robber([1, 1, 1]))
    test(0, house_robber([]))
    test(0, house_robber([0]))
    test(1, house_robber([1]))
    test(0, house_robber([0, 0]))
    test(2, house_robber([2, 1]))
    test(0, house_robber([0, 0, 0]))
    test(4, house_robber([2, 4, 2]))
    test(2, house_robber([1, 1, 1, 1]))
    test(3, house_robber([2, 1, 1, 1]))
    test(3, house_robber([1, 2, 1, 1]))
    test(3, house_robber([1, 1, 2, 1]))
    test(3, house_robber([1, 1, 1, 2]))
    test(2, house_robber([1, 2, 1, 0]))
    test(11, house_robber([1, 7, 9, 4]))
    test(10, house_robber([2, 9, 7, 1]))
    test(26, house_robber([2, 1, 2, 6, 1, 8, 10, 10]))

if __name__ == "__main__":
    main()

