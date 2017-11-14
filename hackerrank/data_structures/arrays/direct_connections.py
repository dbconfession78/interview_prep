#!/usr/bin/python3

T = int(input().strip())
scen = []
for i in range(T):
    N = int(input().strip())
    coords = [int(x) for x in input().strip().split(' ')]
    pop = [int(x) for x in input().strip().split(' ')]

    # zip keeps elements of pop tied to elems in sorted coords
    pop = [x for _,x in sorted(zip(coords, pop))]
    coords = sorted(coords)

    print(coords)
    input(pop)
    required = 0
    _dict = {'coords': coords, 'pop': pop, 'required': required, 'size':N}
    scen.append(_dict)

for s in scen:
    N = s.get('size')
    coords = s.get('coords')
    pop = s.get('pop')
    required = s.get('required')
    for i in range(N):
        for j in range(i, N):
            if i != j:
                required += max(pop[i], pop[j]) * (abs(coords[i] - coords[j]))
    print(required % 1000000007)


