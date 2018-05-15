"""
Check if A × B = C.
A, B and C are string representations of binary square matrices.
n is the size of the n × n matrices.

Example
For a = "1111", b = "1010", c = "1001" and n = 2, the output should be
matrixCheck(a, b, c, n) = false.

A = 1, 1
    1, 1
B = 1, 0
    1, 0
A x B =
(1)(1)+(1)(1), (1)(0)+(1)(0) = 1+1,0+0 = 0,0
(1)(1)+(1)(1), (1)(0)+(1)(0) = 1+1,0+0 = 0,0
C = 1, 0
    0, 1
A x B != C.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string a

String representation of n × n binary matrix.

[input] string b

String representation of n × n binary matrix.

[input] string c

String representation of n × n binary matrix.

[input] integer n

Guaranteed constraints:
0 < n ≤ 500.

[output] boolean


"""


def matrixCheck(a, b, c, n):
    mtxa = build_matrix(a, n)
    mtxb = build_matrix(b, n)
    mtxc = build_matrix(c, n)
    prod = []

    print("a: {}".format(mtxa))
    print("b: {}".format(mtxb))
    print("c: {}".format(mtxc))

    print(int('001', 2))
    print(int('011', 2))
    print(int('010', 2))

    final = []
    for i in range(len(mtxa)):
        wrd_a = mtxa[i]
        for x in range(len(mtxb)):
            wrd_b = mtxb[i]
            res = []
            for j, a_char in enumerate(wrd_a):
                _this = 0
                for k, b_char in enumerate(wrd_b):
                    a_int = int(a_char)
                    b_int = int(b_char)
                    p = a_int * b_int
                    _this += p
                res.append(_this)
            final.append(res)





def build_matrix(s, n):
    retval = []
    start = 0
    end = n
    for end in range(n, len(s)+n, n):
        retval.append(s[start:end])
        start = end

    return retval




def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0


def main():
    retval = matrixCheck("010001110", "001011010", "011010010", 3)
    test(retval, True)

if __name__ == '__main__':
    main()