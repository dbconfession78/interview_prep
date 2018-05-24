"""
Time Planner

Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting
duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common
time slot that satisfies the duration requirement, return null.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have
elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first
epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable
ur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by
an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a
person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: null # since there is no common slot whose duration is 12

Constraints:

    [time limit] 5000ms

    [input] array.array.integer slotsA
        1 ≤ slotsA.length ≤ 100
        slotsA[i].length = 2

    [input] array.array.integer slotsB
        1 ≤ slotsB.length ≤ 100
        slotsB[i].length = 2

    [input] integer

    [output] array.integer
"""

from sgk_test import test
# def meeting_planner_PRACTICE(slotsA, slotsB, dur):   #
def meeting_planner(slotsA, slotsB, dur):
    i = j = 0
    lenA = len(slotsA)
    lenB = len(slotsB)
    while i < lenA and j < lenB:
        gap = findGap(slotsA[i], slotsB[j])
        if gap >= dur:
            maxstart = max(slotsA[i][0], slotsB[j][0])
            endtime = maxstart + dur
            return [maxstart, endtime]
        if slotsB[j][1] < slotsA[i][1]:
            j += 1
        else:
            i += 1
    return []

def findGap(subA, subB):
    Astart = subA[0]
    Aend = subA[1]
    Bstart = subB[0]
    Bend = subB[1]
    maxstart = max(Astart, Bstart)
    minend = min(Aend, Bend)
    gap = minend - maxstart
    return gap

def meeting_planner_PASSED(slotsA, slotsB, dur):   #
# def meeting_planner(slotsA, slotsB, dur):   #
    def get_intersection(winA, winB):   #
        s = max(winA[0], winB[0]) #
        e = min(winA[1], winB[1]) #
        if s >= e:
            return None
        return [s, e]

    iA = 0  #
    iB = 0  #
    while iA < len(slotsA) and iB < len(slotsB):
        winA = slotsA[iA]   #
        winB = slotsB[iB]   #
        intersection = get_intersection(winA, winB) #
        if intersection and (intersection[0] + dur <= intersection[1]):
            return [intersection[0], intersection[0] + dur]
        if winA[1] <= winB[1]:
            iA += 1
        else:
            iB += 1

    return []



def main():
    ######### TESTS ############
    # test([], meeting_planner([[7,12]], [[2,11]], 5))
    test([6,11], meeting_planner([[6,12]], [[2,11]], 5))
    test([5,7], meeting_planner([[1,10]], [[2,3],[5,7]], 2))
    test([], meeting_planner([[0,5],[50,70],[120,125]], [[0,50]], 8))
    test([60, 68], meeting_planner([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))
    test([60, 72], meeting_planner([[10,50],[60,120],[140,210]], [[0,15],[60,72]], 12))

if __name__ == "__main__":
    main()

