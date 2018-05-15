"""
Robots are attacking!!!

Fortunately, they aren't programmed very well and they are approaching in a single row, standing abreast of one another.

Also, you happen to have a Red Ryder BB gun (don't shoot your eye out).

Each robot has an armor value > 0.

Your BB gun can do 1 damage to any robot.

When a robot's armor drops below 1. It blows up, doing 2 damage to the robots next to it.

It's up to you to stop the invasion, but... BB ammo is expensive.

Given a list of robot armor values robots, return the number representing the fewest amount of shots needed to destroy all of the robots.

Note: robots[n] = 0 indicates that there is no robot in that position.

Example

For robots = [1, 2], the output should be
robotAttack(robots) = 1.
You shoot robots[0] for 1 damage. It blows up taking out the robot next to it for 2 damage.

For robots = [3, 3, 3], the output should be
robotAttack(robots) = 5.
You shoot robots[0] for 1 damage.
robots: [2, 3, 3]
You shoot robots[1] for 1 damage.
robots: [2, 2, 3]
You shoot robots[2] for 1 damage.
robots: [2, 2, 2]
You shoot robots[0] for 1 damage.
robots: [1, 2, 2]
You shoot robots[0] for 1 damage.
It blows up, doing 2 damage to robots[1].
robots[1] blows up doing 2 damage to robots[2].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer robots

The list representing the armor values of the robots.

Guaranteed constraints:
0 < robots.length ≤ 5 · 104,
0 ≤ robots[i] ≤ 200.

[output] integer

The smallest number of shots required to destroy all the robots
"""

from collections import defaultdict
def robotAttack(robots):
    _len = len(robots)
    map = defaultdict(list)
    dead = set()
    shots = 0

    def chain(mn, robots, map, idx, dmg):
        if idx >= len(robots)-1 or idx < 0 or robots[idx] == 0 or (robots[idx-1] < 1 and robots[idx+1] < 1):
            return robots
        robots[idx] -= dmg
        if map[robots[idx]+dmg]:
            map[robots[idx]+dmg].pop(0)
        if robots[idx] > 0:
            map[robots[idx]].append(idx)

        if robots[idx] < 1:
            robots = chain(mn, robots, map, idx-1, 2)
            robots = chain(mn, robots, map, idx+1, 2)
        return robots


    for x in range(len(robots)):
        map[robots[x]].append(x)

    while sum(robots) > 0:
        shots += 1
        mn = min(map.keys())
        idx = map[mn][0]
        # robots[idx] -= 1
        # if robots[idx] > 1:
        #     dead.add(idx)
        robots = chain(mn, robots, map, idx, 1)
            # if idx > 0:
            #     robots[idx-1] -= 2
            # if idx < _len:
            #     robots[idx+1] -= 2
        # map[mn].pop(0)
        # map[robots[idx]].append(idx)
        print(robots)
    return shots




# print(robotAttack([1,2,1,2,1]))
print(robotAttack([3,3,3]))