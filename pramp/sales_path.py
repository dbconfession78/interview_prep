"""
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary).
The root is the company itself, and every node in the tree represents a car distributor that receives cars from the
parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers.
In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:


                      __0_____
                     /  |     \
                   5    3     6
                  /    / \   / \
                 4    2  0  1  5
                     /   |
                    1    10
                    |
                    1
A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales
Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one
Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function
getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and
0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer
"""
"""
                      __0_____
                     /  |     \
                   5    3     6
                  /    / \   / \
                 4    2  0  1  5
                     /   |  
                    1    10
                    |
                    1   
"""
from sgk_test import test
class Node:
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

class Solution():
    # def get_cheapest_cost_PRACTICE(self, rootNode):
    def get_cheapest_cost(self, rootNode):
        return


    def get_cheapest_cost_PASSED(self, rootNode):
    # def get_cheapest_cost(self, rootNode):
        stk = [(rootNode, 0)]
        min_cost = float('inf')
        while stk:
            top, cost = stk.pop()

            if top.children == []:
                cost = cost + top.cost
                min_cost = min(min_cost, cost)
                continue

            for child in top.children:
                stk.append((child, cost + top.cost))

        return min_cost


def main():
    """
                          __0_____
                         /  |     \
                       5    3     6
                      /    / \   / \
                     4    2  0  1  5
                         /   |
                        1    10
                        |
                        1
    """
    root = Node(0)
    n1 = Node(5)
    n1a = Node(4)
    n1.children = [n1a]
    n2 = Node(3)
    n2a = Node(2)
    n2b = Node(0)
    n2.children = [n2a, n2b]
    n3 = Node(6)
    chldrn = [Node(1), Node(5)]
    n3.children = chldrn
    root.children = [n1, n2, n3]
    test(3, Solution().get_cheapest_cost(root))


    n2aa = Node(1)
    n2a.children = [n2aa]
    n2ab = Node(1)
    n2aa.children = [n2ab]
    n2d = Node(10)
    n2b.children = [n2d]
    test(7, Solution().get_cheapest_cost(root))


if __name__ == '__main__':
    main()
