# def findProfession_2(level, pos):
from math import ceil
def findProfession(level, pos):
    p = pos
    i = 1
    path = []
    while i <= level:
        p = ceil(p / i)
        if p % 2 == 0:
            path.insert(0, "right")
        else:
            path.insert(0, "left")
        i += 1

    node = "Engineer"
    for elem in path:
        if node == "Engineer":
            if elem == "left":
                node = "Engineer"
            else:
                node = "Doctor"
        else:
            if elem == "left":
                node = "Doctor"
            else:
                node = "Engineer"
    return node





def flip(a):
    dct = {a[1]: a[0], a[0]: a[1]}
    new = []
    for elem in a:
        new.append(dct[elem])
    return a+''.join(new)

def sand(obj):
    second_half = obj[len(obj)//2:]
    first_half = obj[:len(obj)//2]
    new = first_half + second_half + second_half + first_half
    return new

def findProfession_1(level, pos):
# def findProfession(level, pos):
    lvl = 0
    stk = [["E"]]

    while stk:
        lvl += 1
        next_row = []
        row = stk.pop()
        if lvl == level:
            symb = row[pos-1]
            return "Doctor" if symb == "D" else "Engineer"
        _len = len(row)
        i = 0
        while i < _len:
            node = row[i]
            if node:
                if node == "E":
                    l = "E"
                    r = "D"
                else:
                    l = "D"
                    r = "E"
                for child in l, r:
                    next_row.append(child)
            i += 1
        stk.append(next_row)

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
   retval = findProfession(3,3)
   test(retval, "Doctor")

   retval = findProfession(4,2)
   test(retval, "Doctor")

   retval = findProfession(1,1)
   test(retval, "Engineer")

   retval = findProfession(8,100)
   test(retval, "Engineer")

   retval = findProfession(10,470)
   test(retval, "Engineer")

   retval = findProfession(25,16777216)
   test(retval, "Engineer")



   retval = findProfession(4,9)
   test(retval, "Doctor")


if __name__ == '__main__':
    main()