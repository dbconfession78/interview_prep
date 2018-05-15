# Instructions
"""
Given a list representing temepratures on consecutive days, record the number of days it takes for each day's temperature to go above that particular temp.

e.g.
input:  [78, 68, 65, 72, 70]
output: [0, 2, 1, 0, 0]

Explanation:
day 1: The temp is 78 and never goes back up above 78, so we record 0.
day 2: The temp is 68 and takes 2 days before it goes higher than that (day 4: 72 deg)
day 3: The temp is 65 and takes 1 day to go above that (day 4: 72 deg)
day 4: The temp is 72 and never goes abover that so we record 0
day 5: The temp is 70 degrees. Since it is the last day, we record 0

"""
class Solution:
    def temperature_ranges_PRACTICE(self, temps):
    # def temperature_ranges(self, temps):
        return


    def temperature_ranges_MINE(self, temps):
    # def temperature_ranges(self, temps):
        stk = []
        retlst = [0 for x in range(len(temps))]
        for i, temp in enumerate(temps):
            while stk and temps[stk[-1]] < temp:
                idx = stk.pop()
                retlst[idx] = i - idx
            stk.append(i)
        return retlst

def main():
    print(Solution().temperature_ranges([78, 68, 65, 72, 70]))  # [0, 2, 1, 0, 0]
    print(Solution().temperature_ranges([70, 71, 68, 67, 75]))  # [1, 3, 2, 1, 0]
    print(Solution().temperature_ranges([676, 562, 820, 563, 333, 259, 145, 930, 952, 613]))    # [2, 1, 5, 4, 3, 2, 1, 1, 0, 0]

if __name__ == "__main__":
    main()