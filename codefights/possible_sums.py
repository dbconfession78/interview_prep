"""
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
possibleSums(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer coins

An array containing the values of the coins in your collection.

Guaranteed constraints:
1 ≤ coins.length ≤ 20,
1 ≤ coins[i] ≤ 104.

[input] array.integer quantity

An array containing the quantity of each type of coin in your collection. quantity[i] indicates the number of coins that have a value of coins[i].

Guaranteed constraints:
quantity.length = coins.length,
1 ≤ quantity[i] ≤ 105.

It is guaranteed that (quantity[0] + 1) * (quantity[1] + 1) * ... * (quantity[quantity.length - 1] + 1) <= 106.

[output] integer

The number of different possible sums that can be created from non-empty groupings of your coins.
"""
from collections import defaultdict
# def possibleSums_2(coins, quantity):
def possibleSums(coins, quantity):
    max_q = max(quantity)
    idx_max_q = quantity.index(max_q)
    one_coin = max_q * coins[idx_max_q]
    s = set()
    for i, elem in enumerate(quantity):
        for v in s:
            s[v] += elem
    print()
    s.add(one_coin)

    copy = {x for x in s}


    print()

"""
calculate one coin, preferably one with max quantity
drop this into a hashset
calculate each other coin and it's quantity
a) copy your hashset
b) add the value for each quantity to all the values in hashset
c) along with zero and along with coin value
d) do loop ignoring coin originally calculated in 1 (index)
e) set original hashset to copied hashset (rinse and repeat for each quantity)
return hashset count -1 (ignore zero)
"""
def possibleSums_1(coins, quantity):
# def possibleSums(coins, quantity):
    stk = [quantity]
    sum_set = set()
    retval = 0
    while stk:
        top = stk.pop()
        _len = len(top)
        i = 0
        while i < _len:
            s = 0
            new = [x for x in top]
            for j, elem in enumerate(coins):
                s += elem * top[j]
            if s > 0:
                if s not in sum_set:
                    retval += 1
                    sum_set.add(s)
                if new[i] > 0:
                    new[i] -= 1
                    stk.append(new)
            i += 1
    return len(sum_set)

def main():
    print(possibleSums([10,50,100], [1,2,1]))


if __name__ == '__main__':
    main()

