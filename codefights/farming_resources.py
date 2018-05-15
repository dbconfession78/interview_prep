"""
You decide to send your troops to the Logging Camp to gather some lumber. Like any good Commander, you first need to make sure that your enemy's troops (which are heading to the same Logging Camp) won't get there first.

The world map can be represented as an infinite grid of hexagonal cells (a Hex Map). Each cell is uniquely defined by its coordinates as shown below:

Your troops, your enemy's troops and the Logging Camp each occupies exactly one cell.

There are 2 types of cells, those that are passable and those that are impassable. Troops can move from one passable cell to another if they share a common side. Such a move takes k seconds where k represents the size of the troops.

Both you and your enemy are so eager to get to the Logging Camp that you ignore each other's troop movements. In other words, you can both safely occupy the same cell at the same time (including the initial cell).

Given the locations of the troops and the Logging Camp, find out if your troops can reach their destination earlier than your enemy.

Example

    For friendlyTroops = [-2, 2, 3], enemyTroops = [1, 0, 9], loggingCamp = [0, 0] and impassableCells = [[-1, 1]], the output should be
    farmingResources(friendlyTroops, enemyTroops, loggingCamp, impassableCells) = false.

    Your troops need 3 * 3 = 9 seconds to reach the Logging Camp (one of the optimal paths is (-2, 2) -> (-2, 1) -> (-1, 0) -> (0, 0), i.e. 3 marches taking 3 seconds each). Your enemy's troops will arrive in 9 * 1 = 9 (1 march taking 9 seconds) seconds as well.

    For the same friendlyTroops, enemyTroops and loggingCamp, and impassableCells = [], the output should be
    farmingResources(friendlyTroops, enemyTroops, loggingCamp, impassableCells) = true.

    Your troops need 3 * 2 = 6 seconds to reach the Logging Camp (the optimal paths is (-2, 2) -> (-1, 1) -> (0, 0), i.e. 2 marches taking 3 seconds each). Your enemy's troops will arrive in only 9 seconds.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer friendlyTroops

    Array of three integers: the first two values represent the location of your troops; the third, its size (a positive integer).

    Guaranteed constraints:
    friendlyTroops.length = 3,
    -20 < friendlyTroops[0], friendlyTroops[1] < 20,
    1 ≤ friendlyTroops[2] < 20.

    [input] array.integer enemyTroops

    Array of three integers: the first two values represent the location of your enemy's troops; the third, its size (a positive integer).

    Guaranteed constraints:
    enemyTroops.length = 3,
    -20 < enemyTroops[0], enemyTroops[1] < 20,
    1 ≤ enemyTroops[2] < 20.

    [input] array.integer loggingCamp

    Array of two integers representing the location of the Logging Camp. It's guaranteed that neither your troops nor your enemy's troops are initially in the Logging Camp cell.

    Guaranteed constraints:
    loggingCamp.length = 2,
    -20 < loggingCamp[i] < 20.

    [input] array.array.integer impassableCells

    Each element of impassableCells is an array of two integers describing the coordinates of an impassable cell. It's guaranteed that for both your troops and your enemy troops it's possible to reach the Logging Camp.

    Guaranteed constraints:
    0 ≤ impassableCells.length ≤ 40,
    impassableCells[i].length = 2,
    -20 < impassableCells[i][j] < 20.

    [output] boolean

    true if your troops can get to the Logging Camp before your enemy, false otherwise.
"""
test_no = 1
impass = set()
seen = set()

def farmingResources(friendlyTroops, enemyTroops, loggingCamp, impassableCells):
    global impass

    def dfs(curr, end, troops, retval):
        if curr == end:
            return retval + troops
        if curr in impass:
            return retval

        i = curr[0]
        j = curr[1]
        if end[0] != i:
            retval += troops
        if end[1] != j:
            retval += troops

        if end[0] < i:
            i -= 1
        elif end[0] > i:
            i += 1

        if end[1] < j:
            j -= 1
        elif end[1] > j:
            j += 1

        return dfs([i, j], end, troops, retval)

    impass = set(tuple(x) for x in impassableCells)
    f_coor = [friendlyTroops[0], friendlyTroops[1]]
    e_coor = [enemyTroops[0], enemyTroops[1]]
    f_troops = friendlyTroops[2]
    e_troops = enemyTroops[2]

    f = dfs(f_coor, loggingCamp, f_troops, 0)
    e = dfs(e_coor, loggingCamp, e_troops, 0)
    return f < e



def farmingResources_2(friendlyTroops, enemyTroops, loggingCamp, impassableCells):
    global impass

    fncs = [get_times_impass, get_times_no_impass]
    impass = set(tuple(x) for x in impassableCells)
    f_coor = [friendlyTroops[0], friendlyTroops[1]]
    e_coor = [enemyTroops[0], enemyTroops[1]]
    f_troops = friendlyTroops[2]
    e_troops = enemyTroops[2]

    fnc = fncs[0]
    if impassableCells == [[]]:
        fnc = fncs[1]

    f_time = fnc(f_coor, loggingCamp, f_troops)
    e_time = fnc(e_coor, loggingCamp, e_troops)
    return f_time < e_time

def check_surround(coord, end):
    i = coord[0]
    j = coord[1]
    dirs = {(i, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j + 1),
            (i + 1, j),
            (i + 1, j - 1)
            }
    return tuple(end) in dirs


def get_dist(start, end):
    retval = 0
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]

    curr = list(start)
    while curr != list(end):
        if check_surround(curr, end):
            return retval + 1
        # if curr[0]+1 == end[0] or curr[0]-1 == end[0]:
        #     if curr[1]+1 == end[1] or curr[1]-1 == end[1]:
        #         return retval + 1
        # if curr[1]+1 == end[1] or curr[1]-1 == end[1]:
        #     if
        if curr[0] != end[0]:
            if end[0] < curr[0]:
                curr[0] -= 1
            elif end[0] > curr[0]:
                curr[0] += 1
        elif curr[1] != end[1]:
            if end[1] < curr[1]:
                curr[1] -= 1
            elif end[1] > curr[1]:
                curr[1] += 1
        retval += 1
    return retval

def get_times_no_impass(start, end, troops):
    curr = start
    retval = 0
    while curr[0] != end[0]:
        if end[0] < curr[0]:
            curr[0] -= 1
        else:
            curr[0] += 1
        retval += troops

    while curr[1] != end[1]:
        if end[1] < curr[1]:
            curr[1] -= 1
        else:
            curr[1] += 1
        retval += troops

    return retval



def get_times_impass(start, end, troops):
    global impass
    global seen

    seen = set()
    seen.add(tuple(start))
    retval = 0
    stk = [(start, 0)]
    dct = {}
    while stk:
        coord, time = stk.pop()
        i = coord[0]
        j = coord[1]
        dirs = {"UL": [i, j - 1],
                "L": [i - 1, j],
                "DL": [i - 1, j + 1],
                "DR": [i, j + 1],
                "R": [i + 1, j],
                "UR": [i + 1, j - 1]
                }
        # dist_from_here = [abs(end[0] - coord[0]), abs(end[1] - coord[1])]
        # dist_from_here_i = dist_from_here[0]
        # dist_from_here_j = dist_from_here[1]
        dupe_coord = coord
        # print()
        if tuple(coord) in dct:
            here_to_lc = list(dct[tuple(coord)])
        else:
            here_to_lc = get_dist(coord, end)
            dct[tuple(coord)] = here_to_lc
        for k, v in dirs.items():
            if tuple(v) not in seen:
                if tuple(v) not in impass:
                    if v == end:
                        return time + troops
                    else:
                        # print("here: {}".format(coord))
                        # print("{}: {}".format(k, v))
                        # print("log: {}".format(end))

                        # dist_from_dir_i = abs(end[0] - v[0])
                        # dist_from_dir_j = abs(end[1] - v[1])

                        ########### TEST START #############
                        if tuple(v) in dct:
                            dir_to_lc = dct[tuple(v)]
                        else:
                            dir_to_lc = get_dist(v, end)
                        if dir_to_lc <= here_to_lc:
                            stk.insert(0, ((v, time + troops)))
                        # print()
                        ########### TEST END #############


                        # if dist_from_dir_i <= dist_from_here_i:
                            # if dist_from_dir_j <= dist_from_here_j:
                            # stk.insert(0, ((v, time + troops)))
                        # elif dist_from_dir_j <= dist_from_here_j:
                            # if dist_from_dir_i <= dist_from_here_i:
                            # stk.insert(0, ((v, time + troops)))

                # else:
                #     if tuple(v) in impass:
                #         if (v[0] - 1, v[1]) not in impass:
                #             stk.insert(0, ([v[0]+1, v[1]], time + troops))
                seen.add(tuple(v))


    return retval

def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))

test(False, farmingResources([-2, 2, 3], [1, 0, 9], [0, 0], [[-1, 1]]))
test(True, farmingResources([-2, 2, 3], [1, 0, 9], [0, 0], [[]]))
test(False, farmingResources([2, -1, 19], [0, 3, 9], [1, 1], [[0, 2], [1, 2]]))
test(True, farmingResources([2, -1, 19], [0, 3, 10], [1, 1], [[0, 2], [1, 2]]))
test(True, farmingResources([-2, 2, 3], [1, 0, 8], [0, 0], [[]]))
test(False, farmingResources([0, -3, 1], [2, -3, 1], [-3, 0], [[-1, -2], [-2, -1], [-2, 0], [-3, -1]]))
test(True, farmingResources([18, 18, 1], [19, 19, 1], [-19, -19], [[]]))
test(True, farmingResources([17, 18, 6], [19, 16, 6], [18, 19], [[17, 19], [18, 18], [19, 18]]))
test(False, farmingResources([19, 19, 1], [8, 9, 19], [9, 9], [[9, 10], [8, 10], [8, 8], [8, 7]]))
test(True, farmingResources([19, 19, 1], [10, 9, 19], [11, 9], [[9, 10], [8, 10], [8, 8], [8, 7]]))
#
# # my_tests
test(True, farmingResources([1, 1, 5], [1, 1, 6], [11, 9], [[9, 10], [8, 10], [8, 8], [8, 7]]))
test(False, farmingResources([1, 1, 7], [1, 1, 6], [11, 9], [[9, 10], [8, 10], [8, 8], [8, 7]]))