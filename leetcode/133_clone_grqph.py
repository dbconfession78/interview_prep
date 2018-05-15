# Instructions
"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # def cloneGraph_PRACTICE(self, node):
    def cloneGraph(self, node):
        return

    def cloneGraph_PASSED(self, node):
    # def cloneGraph(self, node):
        if not node:
            return node

        _map = {}
        root = UndirectedGraphNode(node.label)
        stk = [node]
        _map[root.label] = root

        while stk:
            top = stk.pop()
            for neigh in top.neighbors:
                if neigh.label not in _map:
                    _map[neigh.label] = UndirectedGraphNode(neigh.label)
                    stk.append(neigh)
                _map[top.label].neighbors.append(_map[neigh.label])
        return root


def main():
    node = UndirectedGraphNode(0)
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n3 = UndirectedGraphNode(3)
    n4 = UndirectedGraphNode(4)
    n5 = UndirectedGraphNode(5)
    node.neighbors = [n1, n2, node]
    n1.neighbors = [n2]
    n2.neighbors = [n2, n3, node]
    n3.neighbors = [n1, n2, n4]
    n4.neighbors = [n5]
    n5.neighbors = [n1, node]
    clone = Solution().cloneGraph(node)
    print(f'root: ({clone.label}) {[x.label for x in clone.neighbors]}')
    r1 = clone.neighbors[0]
    print(f'r1: ({r1.label}) {[x.label for x in r1.neighbors]}')

    r2 = clone.neighbors[1]
    print(f'r2: ({r2.label}) {[x.label for x in r2.neighbors]}')

    r3 = clone.neighbors[1].neighbors[1]
    print(f'r3: ({r3.label}) {[x.label for x in r3.neighbors]}')

    r4 = clone.neighbors[1].neighbors[1].neighbors[2]
    print(f'r4: ({r4.label}) {[x.label for x in r4.neighbors]}')

    r5 = clone.neighbors[1].neighbors[1].neighbors[2].neighbors[0]
    print(f'r5: ({r5.label}) {[x.label for x in r5.neighbors]}')

# expected:
# root: (0) [1, 2, 0]
# r1: (1) [2]
# r2: (2) [2, 3, 0]
# r3: (3) [1, 2, 4]
# r4: (4) [5]
# r5: (5) [1, 0]




if __name__ == '__main__':
    main()
