import sys
import os
from  urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
# import urllib.request
# import urllib.parse


from collections import defaultdict
class Solution:
    def func1(self, lst):
        high = 0
        results = defaultdict(int)
        for elem in lst:
            results[elem] += 1
            if results[elem] > high:
                high = results[elem]

        # _max = max(results.values())
        winners = sorted([k for k,v in results.items() if v == high])
        return winners[-1]

    def getNumberOfMovies(self, substr):
        return
        # result = json.loads(res.readall().decode('utf-8'))
        # url = "https://jsonmock.hackerrank.com/api/movies/search/?Title="
        # req = Request("{}{}".format(url, substr))
        # res = urlopen(req)
        # retval = 0
        # if res:
        #     dct = json.load(res)
        #     retval = dct.get("total")
        # return retval

    # def waitingTime_2(self, tickets, p):
    def waitingTime(self, tickets, p):
        return
        time = 0



    def waitingTime_1(self, tickets, p):
    # def waitingTime(self, tickets, p):
        req = tickets[p]
        to_front = p
        time = 0
        while True:
            for i, elem in enumerate(tickets):
                if tickets[i] > 0:
                    time += 1
                    tickets[i] -= 1
                    if tickets[i] == 0:
                        if i == p:
                            return time





def main():
    lst = ["Joe", "Mary", "Mary", "Joe"]
    # print(Solution().getNumberOfMovies("maze"))
    print(Solution().waitingTime([1,2,5], 1))


if __name__ == '__main__':
    main()

"""
class Solution:
    def func(self):
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
