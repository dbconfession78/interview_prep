"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
from collections import defaultdict


class Solution:
    def __init__(self, sol):
        self.sol = sol
    # def findItinerary_4(self, tickets):
    def findItinerary(self, tickets):
        dct1 = defaultdict(list)
        route = []
        for i, elem in enumerate(sorted(tickets)[::-1]):
            dct1[elem[0]].append(elem[1])


        def visit(next):
            while dct1[next]:
                visit(dct1[next].pop())
                # next = dct1.get(next).pop()
            route.append(next)
        visit("JFK")
        return route[::-1]




    def findItinerary_3(self, tickets):
    # def findItinerary(self, tickets):
        dct1 = defaultdict(list)
        route = []
        for k, v in sorted(tickets)[::-1]:
            dct1[k].append(v)

        def visit(next):
            while dct1[next]:
                visit(dct1[next].pop())
                # dct1[next].pop(dct1[next].index(next))
            route.append(next)

        visit("JFK")
        return route[::-1]

    def findItinerary_SOL(self, tickets):
    # def findItinerary(self, tickets):

        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dct1 = defaultdict(list)
        route = []

        for a, b in sorted(tickets)[::-1]:
            dct1[a] += b


        def visit(airport):
            while dct1[airport]:
                visit(dct1[airport].pop())
            route.append(airport)
        visit("JFK")
        return route[::-1]


    def test(self, retval):
        if retval != self.sol:
            print("FAIL: ")
            print(f"retval: {retval}")
            print(f"expected: {self.sol}")
            return -1
        print("OK")
        return 0

def main():
    sol = Solution(["JFK","MUC","LHR","SFO","SJC"])
    retval = sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
    sol.test(retval)

    sol = Solution(["JFK","ATL","JFK","SFO","ATL","SFO"])
    retval = sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    sol.test(retval)

    sol = Solution(["JFK","NRT","JFK","KUL"])
    retval = sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    sol.test(retval)

    sol = Solution(["JFK","ATL","PHX","LAX","JFK","ORD","PHL","ATL"])
    retval = sol.findItinerary([["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]])
    sol.test(retval)

    sol = Solution(["JFK","ATL","JFK"])
    retval = sol.findItinerary([["JFK","ATL"],["ATL","JFK"]])
    sol.test(retval)

# LC Input
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# [["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]]
# [["JFK","ATL"],["ATL","JFK"]]
if __name__ == '__main__':
    main()

