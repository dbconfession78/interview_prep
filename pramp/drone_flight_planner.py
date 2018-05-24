"""
Drone Flight Planner

You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm that calculates the minimum amount of energy required for the company’s drone to complete its flight. You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, and it gains 1 kWh for every mile it descends. Flying sideways neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone would need to complete its route. Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.

For simplicity, every 3D point will be represented as an integer array whose length is 3. Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:

input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy

Constraints:

    [time limit] 5000ms

    [input] array.array.integer route
        1 ≤ route.length ≤ 100

    [output] integer

"""


# sgkur04@gmail.com
# https://www.linkedin.com/in/stuart-kuredjian-8100a273/
# linkedin sales navigator
# Akshay Agarwal

# def calc_drone_min_energy_PRACTICE(route):
def distance(p1, p2):
  return sum((x - y)**2 for x, y in zip(p1, p2))


def calc_drone_min_energy(route):
  if len(route) < 3: return 0
  total = 0
  for i in xrange(1, len(route)):
    prev = route[i - 1]
    asc = route[i][-1] > prev[-1]
    dsc = route[i][-1] < prev[-1]
    if asc:
      total += distance(route[i], prev)
    elif dsc:
      total -= distance(route[i], prev)
  return total if total > 0 else 0

route = [ [0,   2, 10], [3,   5,  0], [9,  20,  6], [10, 12, 15], [10, 10,  8] ]
print

def calc_drone_min_energy_PASSED(route):
# def calc_drone_min_energy(route):
    _len = len(route)
    i = 0
    _min = route[0][2]
    _max = route[0][2]

    while i < _len:
        curr = route[i][2]
        _max = max(_max, curr)
        i += 1
    return _max - _min


def main():
    # 5
    print(calc_drone_min_energy([[0, 2, 10],
                                 [3, 5, 0],
                                 [9, 20, 6],
                                 [10, 12, 15],
                                 [10, 10, 8]]))
    # 0
    print(calc_drone_min_energy([[0,1,19]]))

    # 0
    print(calc_drone_min_energy([[0,2,10],
                                  [10,10,8]]))

    # 14
    print(calc_drone_min_energy([[0,2,6],
                                 [10,10,20]]))

    # 5
    print(calc_drone_min_energy([[0,2,10],
                                 [3,5,0],
                                 [9,20,6],
                                 [10,12,15],
                                 [10,10,8]]))

    # 36
    print(calc_drone_min_energy([[0,2,2],
                                 [3,5,38],
                                 [9,20,6],
                                 [10,12,15],
                                 [10,10,8]]))

    # 0
    print(calc_drone_min_energy([[0,2,10],
                                 [3,5,9],
                                 [9,20,6],
                                 [10,12,2],
                                 [10,10,10],
                                 [10,10,2]]))


if __name__ == "__main__":
    main()

