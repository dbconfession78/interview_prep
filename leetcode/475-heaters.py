# Instructions
"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

def main():
    """test cases """
    # print(heater_rad4([474833169, 264817709, 998097157, 817129560], [197493099, 404280278, 893351816, 505795335]))
    # print(heater_rad([1, 5], [10]))
    print(heater_rad([1], [1, 2, 3, 4, 5]))
    print(heater_rad([1, 2, 3, 4], [1, 4]))
    print(heater_rad([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [2, 4, 7, 11, 14]))
    print(heater_rad([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923], [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840,143542612]))

    # houses = [int(x) for x in input().strip('[],').replace(',', ' ').split(' ')]
    # heaters = [int(x) for x in input().strip('[],').replace(',', ' ').replace(', ', ' ').split(' ')]
    # print(heater_rad(houses, heaters))


def heater_rad(houses, heaters):
    houses.sort()
    heaters.sort()
    i = 0
    j = 0
    res = 0
    while i < len(houses):
        while j < len(heaters)-1 and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
            j += 1
        res = max(res, abs(heaters[j] - houses[i]))
        i += 1
    return res


if __name__ == '__main__':
    main()