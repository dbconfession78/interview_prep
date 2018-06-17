"""
Company Challenge: Instacart
To make sure that groceries can always be delivered, Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.

Each day is divided into several intervals that do not overlap and cover the whole day from 00:00 to 23:59. For each i the delivery fee in the intervals[i] equals fees[i].

Given the list of delivery requests deliveries, your task is to check whether the delivery fee is directly correlated to the order volume in each interval i.e. the interval_fee / interval_deliveries value is constant for each interval throughout the day.

Example

For
intervals = [0, 10, 22], fees = [1, 3, 1] and

deliveries = [[8, 15],
              [12, 21],
              [15, 48],
              [20, 17],
              [23, 43]]
the output should be
deliveryFee(intervals, fees, deliveries) = true.

The day is divided into 3 intervals:

from 00:00 to 09:59, the first delivery was made, fees[0] / 1 = 1;
from 10:00 to 21:59, the 2nd, 3rd and 4th deliveries were made, fees[1] / 3 = 1;
from 22:00 to 23:59, the last delivery was made, fees[2] / 1 = 1.
interval_fee / interval_deliveries = 1 for each interval, so the answer is true.

Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer intervals

Each interval starts at xx:00 and ends at yy:59, where xx equals intervals[i] and yy equals intervals[i + 1] - 1, or 23 if intervals[i + 1] doesn't exist. intervals[i] represents the hour at which the ith interval starts. It is guaranteed that intervals[0] = 0.

Guaranteed constraints:
1 ≤ intervals.length ≤ 24,
0 ≤ intervals[i] ≤ 23,
intervals[0] = 0.

[input] array.integer fees

Array of non-negative integers of the same length as intervals. fees[i] is the delivery fee in the ith interval.

Guaranteed constraints:
fees.length = intervals.length,
0 ≤ fees[i] ≤ 105.

[input] array.array.integer deliveries

Deliveries in the order they were made. Each delivery is represented as the [h, m] array, h is the hour and m is the minute it was done. It is guaranteed that there were no deliveries at the same time.

Guaranteed constraints:
1 ≤ deliveries.length ≤ 30,
0 ≤ deliveries[i][0] ≤ 23,
0 ≤ deliveries[i][1] ≤ 59.

[output] boolean

true if the delivery fee is directly correlated to the order volume in each interval, false otherwise.
"""
from sgk_test import test
def deliveryFee(intervals, fees, deliveries):
    inter_len = len(intervals)
    del_len = len(deliveries)
    inter_idx = 0
    del_idx = 0
    last = None
    count = 0

    while del_idx < del_len:
        deliv = deliveries[del_idx]
        hr = deliv[0]
        mn = deliv[1]
        if inter_idx == inter_len - 1:
            if hr >= intervals[inter_idx]:
                count += del_len - del_idx
                del_idx = del_len
        elif hr < intervals[inter_idx + 1]:
            count += 1
            del_idx += 1
        else:
            if count > 0:
                x = fees[inter_idx] / count
                if last is None:
                    last = x
                else:
                    if x != last:
                        return False
            inter_idx += 1
            count = 0
    if inter_idx < inter_len - 1:
        return False
    x = fees[inter_idx] / count
    if last is not None:
        if x != last:
            return False
    return True




def main():
    ######### TESTS ############
    test(True, deliveryFee([0, 10, 22], [1, 3, 1], [[8,15], [12,21], [15,48], [20,17], [23,43]]))
    test(False, deliveryFee([0, 10, 22], [1, 3, 1], [[8,15], [12,21], [15,48], [20,17]]))
    test(False, deliveryFee([0, 22], [1, 1], [[5,34], [21,23], [23,0], [23,1], [23,59]]))
    test(True, deliveryFee([0], [34343], [[12,34], [14,45], [17,58], [23,25]]))
    test(True, deliveryFee([0, 10, 23], [3, 3, 3], [[0,12], [0,13], [0,51], [9,17], [10,3], [10,59], [22,22], [22,23],
                                                    [23,0], [23,17], [23,47], [23,48]]))
    test(False, deliveryFee([0, 10, 22], [1, 3, 1], [[8,15], [12,21], [15,48], [20,17], [22, 17], [0,43], [1, 20]]))

if __name__ == "__main__":
    main()

