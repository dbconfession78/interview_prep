"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system of his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient for those dark times.

When you started to learn about Byteasar's III deeds in your history classes, the creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in the Byteasar's kingdom, which were connected by the two-ways roads. You managed to get information about this roads from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

Example

For n = 6 and

roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = true.

Here's how the road system can be represented:


For n = 6 and

roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = false.

Here's how the road system can be represented:


As you can see, it's only possible to travel from city 3 to city 4 by traversing at least 3 roads.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

The number of cities in the kingdom.

Guaranteed constraints:
1 ≤ n ≤ 250.

[input] array.array.integer roads

Array of roads in the kingdom. Each road is given as a pair [cityi, cityj], where 0 ≤ cityi, cityj < n and cityi ≠ cityj. It is guaranteed that no road is given twice.

Guaranteed constraints:
0 ≤ roads.length ≤ 35000,
roads[i].length = 2,
0 ≤ roads[i][j] < n.

[output] boolean

true if the road system is efficient, false otherwise.
"""
from collections import defaultdict

# def efficientRoadNetwork_FAILS_LAST_TWO_TIME_LIMIT(n, roads):
def efficientRoadNetwork(n, roads):
    memo = {}
    def is_efficient(n, graph, ori):
        for dest in range(n):
            if (ori, dest) in memo:
                if memo[(ori, dest)] ==  False:
                    return False
            conns = graph[ori]
            if dest == ori:
                continue
            for conn in conns:
                hop_1 = graph[conn]
                conns = conns.union(hop_1)
            if dest not in conns:
                memo[(ori, dest)] = False
                return False
            else:
                memo[(ori,dest)] = True
        return True

    graph = defaultdict(set)
    for road in roads:
        ori = road[0]
        dest = road[1]
        graph[ori].add(dest)
        graph[dest].add(ori)

    for ori in range(n):
        if is_efficient(n, graph, ori) == False:
            return False
    return True

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
   retval = efficientRoadNetwork(7, [[1,0], [0,2], [2,4], [3,0], [5,6], [5,4], [5,0], [0,4], [5,2]])
   test(retval, False)

if __name__ == '__main__':
    main()
