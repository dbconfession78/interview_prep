from random import random
import sys
remain = []
should_hard_code = False
rand = False
all_ones = False


class Node:
    def __init__(self, data, next=None, prev=None, up=None, down=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.up = up
        self.down = down
        self.id = None
        self.level = None
        self.visited = False
        self.row_end = False


class Map:
    def __init__(self, root=None):
        self.root = root
        self.tail = None
        self.size = 0
        self.width = None
        self.dict = {}

    def add(self, data, width):
        if self.width is None:
            self.width = width
        new = Node(data)
        new.id = self.size
        new.level = (self.size // width)

        if self.root is None:
            self.root = new
            self.tail = new
            self.dict[new.id] = new
        else:
            new.prev = self.tail
            if (new.id+1) % self.width == 0:
                new.row_end = True
            self.tail.next = new
            self.tail = self.tail.next
            self.dict[new.id] = new

            # set idx of prev row (up) and next row (down)
            if self.size > width - 1:
                # walk = self.dict.get(new.id - width)
                walk = self.get_node_at_index(self.size - width, True)
                # walk = self.tail
                # i = 0
                # while walk and i < width:
                #     walk = walk.prev
                #     i += 1
                walk.down = self.tail
                self.tail.up = walk

        self.size += 1

    def get_node_at_index(self, index, from_end=None):
        """ option to start from end  """
        if from_end:
            walk = self.tail
            i = self.size
        else:
            walk = self.root
            i = 0
        while walk and i != index:
            if from_end:
                walk = walk.prev
                i -= 1
            else:
                walk = walk.next
                i += 1
        return walk


def main():
    global remain, should_hard_code, rand, all_ones
    """test cases"""
    grid = []
    map = Map()
    if should_hard_code:
        grid = [[0, 0, 1, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1],
                [1, 1, 0, 1, 1, 1]]

        n_rows = len(grid) # hard-code
        n_cols = len(grid[0]) # hard-code
    else:
        n_rows = int(input().strip()) # input
        n_cols = int(input().strip()) # input

    size = n_rows * n_cols
    remain = [x for x in range(size)]

    if all_ones:
        for x in range(size):
            map.add(1, n_cols)

    elif not should_hard_code:
        for i in range(n_rows):
            if rand:
                map_row = [random.choice([0, 1]) for x in range(n_cols)]
            else:
                map_row = [int(x) for x in input().strip().split(' ')] # input
            for elem in map_row:
                map.add(elem, n_cols)

    if should_hard_code and not all_ones:
        i = 0
        while i < n_rows:
            j = 0
            while j < n_cols:
                map.add(grid[i][j]
n_cols)
                j += 1
            i += 1

    walk = map.root
    i = 0
    # while walk:
    #     sys.stdout.write('{} '.format(int(walk.data)))
    #     i += 1
    #     if i % n_cols == 0:
    #         print()
    #     walk = walk.next

    print(explore(map))


def explore(map):
    root = map.root
    big = 0
    walk = root
    while len(remain) != 0:
        # if not walk.visited:
        walk = map.dict.get(remain[0])
        big = max(big, explore_helper(walk, map))
        # walk = walk.next
    return big


def explore_helper(root, _map):
    global remain
    # if root is None or root.visited or root.id not in remain:
    if root is None or root.id not in remain:
        return 0
    if root.data == 0:
        remain.pop(remain.index(root.id))
        return 0
    _id = root.id
    _data = root.data
    if root.visited is not True:
        remain.pop(remain.index(root.id))
        root.visited = True
        count = 1
        root.data = 0

        if root.next:
            if not root.row_end:
                count += explore_helper(root.next.up, _map)
                count += explore_helper(root.next, _map)

        if root.down:
            if not root.row_end:
                count += explore_helper(root.down.next, _map)
            count += explore_helper(root.down, _map)

            if root.prev is not None and not root.prev.row_end:
                count += explore_helper(root.down.prev, _map)

        if root.prev:
            if not root.prev.row_end:
                count += explore_helper(root.prev, _map)

        if root.up:
            if not root.prev.row_end:
                count += explore_helper(root.up.prev, _map)
            count += explore_helper(root.up, _map)

    return count


def is_row_end(width, id):
    if id+1 % width == 0:
        return True
    else:
        return False


# for use with explore_ version
def main_():
    grid = [[0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1]]

    n_rows = int(len(grid))
    n_cols = int(len(grid[0]))
    size = n_rows * n_cols

    grid = []
    i = 0
    while i < 1:
        # for i in range(1):
        grid.append([1 for x in range(991)])
        i += 1
    print(explore(grid))


# this version uses a 2d array instead of a linked list
def explore_(grid):
    i = 0
    big = 0
    for i in range(len(grid)):
        j = 0
        while j < len(grid[0]):
            big = max(big, explore_helper(grid, i, j))
            j += 1
        i += 1
    return big


# for use with explore_ (uses 2d array instead of linked list
def explore_helper_(grid, i, j):
    if not(i in range(len(grid)) and j in range(len(grid[0]))):
        return 0
    # if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid[0]):
    #     return 0
    if grid[i][j] == 0:
        return 0
    count = 1
    grid[i][j] = 0
    # count = grid[i][j] - 1

    count += explore_helper(grid, i - 1, j + 1)
    count += explore_helper(grid, i, j + 1)
    count += explore_helper(grid, i + 1, j + 1)
    count += explore_helper(grid, i + 1, j)

    count += explore_helper(grid, i + 1, j - 1)
    count += explore_helper(grid, i, j - 1)
    count += explore_helper(grid, i - 1, j - 1)
    count += explore_helper(grid, i - 1, j)
    return count


if __name__ == '__main__':
    main()