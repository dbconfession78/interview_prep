#!/usr/bin/python3
import random
import sys
from threading import Thread
import time

size = 8
_map = []


class Node:
    def __init__(self, data):
        self.data = data
        self.explored = False
        self.island_number = 0


def main():
    global _map, is_threading
    _map = build_map(size)
#    _map = build_map(size, True)
    print_map(_map)

    """
    explore(_map, 4, 3)
    _map = explore_north_of(_map, 4, 3)
    print_explored(_map)
    _map = explore_south_of(_map, 4, 3)
    print_explored(_map)
    input()
    _map = explore_east_of(_map, 4, 3)
    print_explored(_map)
    input()

    _map = explore_west_of(_map, 4, 3)
    print_explored(_map)
    input()
    """
    ################### TEST HERE #######################

    print('first: %d' % first)
    while (i < size - 1):

    for i in range(size):
        for j in range(size):
        this = _map[i][j]
        south = get_south_of(i, j)
        east = get_east_of(i, j)
        west = get_west_of(i, j)
        north = get_north_of(i, j)
        if this.data == 1:
            this.explored = True

        if (east != 0 and east != None):
            e_thread = Thread(target=explore_east_of, args=(i, j))
            e_thread.start()
            while e_thread.is_alive():
                print('threading east...')
                if not e_thread.isAlive():
                    e_thread.join()
                    break
            input('here')

        i += 1


def get_south_of(i, j):
    if (i != (size - 1)):
        return (_map[i + 1][j].data)
    return None


def get_east_of(i, j):
    if (j != (size - 1)):
        return (_map[i][j + 1].data)
    return None


def get_north_of(i, j):
    if (i != 0):
        north = _map[i - 1][j].data
        return north
    return None


def get_west_of(i, j):
    if (j != 0):
        return (_map[i][j - 1].data)
    return None


    ####################################################


def explore(i, j):
    explore_south_of(i, j)
    explore_east_of(i, j)
    #    explore_west_of(i, j)

    return _map


def explore_north_of(i, j):
    if i > 0:
        i = i - 1
        while _map[i][j] == 1 and i >= 0 and _map[i][j].explored == False:
            data = _map[i][j].data
            explored = _map[i][j].explored
            print("[{}, {}]: data: {}\nexplored: {}".format(i, j, data, explored))

            explore_branch("east", i, j)
            explore_branch("west", i, j)
            _map[i][j].explored = True
            i -= 1

    return _map


def explore_south_of(i, j):
    if i < size - 1:
        i += 1
        while _map[i][j].data == 1 and i < len(_map) - 1 and _map[i][j].explored == False:
            data = _map[i][j].data
            explored = _map[i][j].explored
            print("[{}, {}]: data: {}\nexplored: {}".format(i, j, data, explored))

            explore_branch("east", i, j)
            explore_branch("west", i, j)
            _map[i][j].explored = True
            i += 1

    return _map


def explore_east_of(i, j):
    if j < size - 1:
        j += 1
        while _map[i][j].data == 1 and j < len(_map) - 1 and _map[i][j].explored == False:
            time.sleep()
            data = _map[i][j].data
            explored = _map[i][j].explored
            _map[i][j].explored = True
            j += 1
            print_explored(_map)
        
        data = _map[i][j].data
        explored = _map[i][j].explored
        _map[i][j].explored = True
        print_explored(_map)
    return _map


def explore_west_of(i, j):
    if i > 0:
        i -= 1
        while _map[i][j].data == 1 and j >= 0 and _map[i][j].explored == False:
            data = _map[i][j].data
            explored = _map[i][j].explored
            print("[{}, {}]: data: {}\nexplored: {}".format(i, j, data, explored))

            explore_branch("north", i, j)
            explore_branch("south", i, j)
            _map[i][j].explored = True
            j -= 1

    return _map


def explore_branch(direction, i, j):
    if direction == "north" and i == 0:
        print('{} index out of range'.format(direction))
        return False

    if direction == "south" and i == size:
        print('{} index out of range'.format(direction))
        return False

    if direction == "east" and j == size - 1:
        return False

    if direction == "west" and i == 0:
        return False

    d = {"north": (explore_north_of, i - 1, j),
         "south": (explore_south_of, i + 1, j),
         "east": (explore_east_of, i, j + 1),
         "west": (explore_west_of, i, j - 1)
         }

    parts = d[direction]
    func = parts[0]
    i = parts[1]
    j = parts[2]
    #    print("{}({}, {})".format(func, i ,j))
    func(i, j)


def print_explored(_map):
    print("\n          EXPLORED")
    sys.stdout.write(' ' * 4)
    for i in range(len(_map)):
        sys.stdout.write("{}  ".format(str(i)))
#        sys.stdout.write("%s  " % str(i))
    print()
    sys.stdout.write(' ' * 3)
    for i in range(len(_map)):
        sys.stdout.write(("-" * 3))
    print()
    for (i, row) in enumerate(_map):
        sys.stdout.write('{} | '.format(i))
#        sys.stdout.write('%d | ' % i)
        for node in row:
            explored = ' '

            if node.data == 1 and node.explored is False:
                explored = '-'
            if node.explored:
                explored = 'X'
            sys.stdout.write("{}  ".format(explored))
        print()


def build_map(size, full=None):
    _map = []
    for i in range(size):
        row = []
        for j in range(size):
            if full:
                row.append(Node(1))
            else:
                row.append(Node(random.choice([0, 1])))
        _map.append(row)
    return _map


def print_map(_map):
    sys.stdout.write(' ' * 4)
    for i in range(len(_map)):
        sys.stdout.write("%s  " % str(i))
    print()
    sys.stdout.write(' ' * 3)
    for i in range(len(_map)):
        sys.stdout.write(("-" * 3))
    print()
    for (i, row) in enumerate(_map):
        sys.stdout.write('%d | ' % i)
        for node in row:
            sys.stdout.write("%s  " % str(node.data))
        print()


def print_row(row):
    for (i, node) in enumerate(row):
        sys.stdout.write(str(row[0].data))


def add_node(row):
    new_node = Node(random.choice([0, 1]))
    row.append(new_node)
    return row


def print_islands(islands):
    for node in islands:
        print(node)


if __name__ == "__main__":
    main()
