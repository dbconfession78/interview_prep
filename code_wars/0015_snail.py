"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
"""

class Solution():
    def snail(self, array):
        _set = set()

        def go_right(array, i, j):
            retpath = []
            if j > len(array[i]) - 1:
                return retpath
            while (i, j) not in _set and j < len(array[i]):
                retpath.append(array[i][j])
                _set.add((i, j))
                j += 1
            return retpath, (i, j)

        def go_down(array, i, j):
            retpath = []
            if i > len(array) - 1:
                return retpath
            while (i, j) not in _set and i < len(array):
                retpath.append(array[i][j])
                _set.add((i, j))
                i += 1
            return retpath, (i, j)

        def go_left(array, i, j):
            retpath = []
            if j < 0:
                return retpath
            while (i, j) not in _set and j >= 0:
                retpath.append(array[i][j])
                _set.add((i, j))
                j -= 1
            return retpath, (i, j)

        def go_up(array, i , j):
            retpath = []
            if i < 0:
                return retpath
            while (i, j) not in _set and j >= 0:
                retpath.append(array[i][j])
                _set.add((i, j))
                i -= 1
            return retpath, (i, j)

        retlst = []
        i = 0
        j = 0
        visited_dir_count = 0

        while True:
            if visited_dir_count == 4:
                return retlst
            visited_dir_count = 0

            disc = go_right(array, i, j)
            if not disc:
                return retlst
            retlst += disc[0]
            i = disc[1][0]+1
            j = disc[1][1]-1
            if not disc[0]:
                visited_dir_count += 1

            disc = go_down(array, i, j)
            if not disc:
                return retlst
            retlst += disc[0]
            i = disc[1][0]-1
            j = disc[1][1]-1
            if not disc[0]:
                visited_dir_count += 1

            disc = go_left(array, i, j)
            if not disc:
                return retlst
            retlst += disc[0]
            i = disc[1][0]-1
            j = disc[1][1]+1
            if not disc[0]:
                visited_dir_count += 1

            disc = go_up(array, i, j)
            if not disc:
                return retlst
            retlst += disc[0]
            i = disc[1][0]+1
            j = disc[1][1]+1
            if not disc[0]:
                visited_dir_count += 1

def main():
    print(Solution().snail([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]
                            ]))         # [1,2,3,6,9,8,7,4,5]
    #
    print(Solution().snail([[1,2,3,1],
                            [4,5,6,4],
                            [7,8,9,7],
                            [7,8,9,7]
                            ]))         # [1,2,3,1,4,7,7,9,8,7,7,4,5,6,4,7,9,8]

    print(Solution().snail([[1,2,3],
                            [8,9,4],
                            [7,6,5]
                            ]))         # [1,2,3,4,5,6,7,8,9]

    print(Solution().snail([[1,2,3,4,5,6,7,8],
                            [9,10,11,12,13,14,15,16],
                            [17,18,19,20,21,22,23,24],
                            [25,26,27,28,29,30,31,32],
                            [33,34,35,36,37,38,39,40],
                            [41,42,43,44,45,46,47,48],
                            [49,50,51,52,53,54,55,56],
                            [57,58,59,60,61,62,63,64]
                            ]))     # ?

    print(Solution().snail([[1,2]]))    # [1,2]






if __name__ == '__main__':
    main()