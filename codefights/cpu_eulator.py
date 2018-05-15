"""
SpaceX is testing flight software subroutines (i.e., programs that consist of sequences of instructions) for a custom
rocket CPU. To ensure that the software runs correctly before it's loaded into the rocket, you need to create a CPU
simulator.

The CPU has 43 32-bit unsigned integer registers, which are named R00..R42. At the start of the program, all the
registers contain 0. The CPU supports the following instructions:

    MOV Rxx,Ryy - copies the value from register Rxx to register Ryy;
    MOV d,Rxx - copies the numeric constant d (specified as a decimal) to register Rxx;
    ADD Rxx,Ryy - calculates (Rxx + Ryy) MOD 2^32 and stores the result in Rxx;
    DEC Rxx - decrements Rxx by one. Decrementing 0 causes an overflow and results in 2^32-1;
    INC Rxx - increments Rxx by one. Incrementing 2^32-1 causes an overflow and results in 0;
    INV Rxx - performs a bitwise inversion of register Rxx;
    JMP d - unconditionally jumps to instruction number d (1-based). d is guaranteed to be a valid instruction number;
    JZ d - jumps to instruction d (1-based) only if R00 contains 0;
    NOP - does nothing.

After the last instruction has been executed, the contents of R42 are considered to be the result of the subroutine.

Write a software emulator for this CPU that executes the subroutines and returns the resulting value from R42.

All the commands in the subroutine are guaranteed to be syntactically correct and have valid register numbers, numeric
constants, and jump addresses. The maximum program length is 1024 instructions. The maximum total number of
instructions that will be executed until the value is returned is 5 · 104. (Keep in mind that the same instruction will
be counted as many times as it will be executed.)

Example

For

subroutine = [
  "MOV 5,R00",
  "MOV 10,R01",
  "JZ 7",
  "ADD R02,R01",
  "DEC R00",
  "JMP 3",
  "MOV R02,R42"
]

the output should be
cpuEmulator(subroutine) = "50".

Here is the information about the CPU state after certain steps:
Step 	Last executed
command 	Non-zero registers 	Comment
1 	1. MOV 5,R00 	R00 = 5 	Put 5 into R00
2 	2. MOV 10,R01 	R00 = 5, R01 = 10 	Put 10 into R01
3 	3. JZ 7 	R00 = 5, R01 = 10 	Move to the next instruction
because R00 ≠ 0
4 	4. ADD R02,R01 	R00 = 5, R01 = 10,
R02 = 10 	R02 += R01
5 	5. DEC R00 	R00 = 4, R01 = 10,
R02 = 10 	R00 -= 1
6 	6. JMP 3 	R00 = 4, R01 = 10,
R02 = 10 	Jump to instruction number 3,
i.e. JZ 7
7 	3. JZ 7 	R00 = 4, R01 = 10,
RO2 = 10 	Move to the next instruction
because R00 ≠ 0
Information about 11 steps is skipped
19 	3. JZ 7 	R00 = 1, R01 = 10,
RO2 = 40 	Move to the next instruction
because R00 ≠ 0
20 	4. ADD R02,R01 	R00 = 1, R01 = 10,
R02 = 50 	R02 += R01
21 	5. DEC R00 	R00 = 0, R01 = 10,
R02 = 50 	R00 -= 1
22 	6. JMP 3 	R00 = 0, R01 = 10,
R02 = 50 	Jump to instruction number 3,
i.e. JZ 7
23 	3. JZ 7 	R00 = 0, R01 = 10,
R02 = 50 	Jump to instruction number 7
because R00 = 0
24 	7. MOV R02,R42 	R00 = 0, R01 = 10,
R02 = 50, R42 = 50 	R42 += R02
The subroutine is exited

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.string subroutine

    Guaranteed constraints:
    1 ≤ subroutine.length ≤ 1024.

    [output] string

    Return the resulting 32-bit unsigned integer, converted into a string.
"""


class CPUEmulator_OTHER:
# class CPUEmulator:
    def __init__(self):
        pass

    def run(self, subroutine):
        # convert to unsigned 32
        def m32(n):
            if n > 4294967295:
                n = n % 4294967295 - 1
            if n < 0:
                n = 4294967295 + (-n) - 1 % 4294967295
            return bin(n)[2:].zfill(32)

        # revert to int
        def u32(b):
            return int(b, 2)

        R = [m32(0)] * 43
        curr_routine = 0

        def MOV(a, b, c):
            if isinstance(a, str):
                R[b] = R[int(a)]
            else:
                R[b] = m32(int(a))
            c += 1
            return c

        def ADD(a, b, c):
            R[a] = m32(u32(R[a]) + u32(R[b]))
            c += 1
            return c

        def DEC(a, c):
            if R[a] == m32(0):
                R[a] = m32(2 ** 32 - 1)
            else:
                R[a] = m32(u32(R[a]) - 1)
            c += 1
            return c

        def INC(a, c):
            if R[a] == m32(2 ** 32 - 1):
                R[a] = m32(0)
            else:
                R[a] = m32(u32(R[a]) + 1)
            c += 1
            return c

        def INV(a, c):
            R[a] = m32(~u32(R[a]))
            c += 1
            return c

        def JMP(d, c):
            c = d - 1
            return c

        def JZ(d, c):
            if R[0] == m32(0):
                c = int(d) - 1
            else:
                c += 1
            return c

        while curr_routine < len(subroutine):
            instruction = subroutine[curr_routine]
            if instruction == "NOP":
                curr_routine += 1
            else:
                f = instruction.split(' ')[0]
                params = instruction.split(' ')[1].split(',')
                for i in range(len(params)):
                    if i == 0 and f == "MOV" and "R" in params[i]:
                        params[i] = str(params[i].replace("R", ""))
                    else:
                        params[i] = int(params[i].replace("R", ""))
                if f == "MOV":
                    curr_routine = MOV(params[0], params[1], curr_routine)
                elif f == "ADD":
                    curr_routine = ADD(params[0], params[1], curr_routine)
                elif f == "DEC":
                    curr_routine = DEC(params[0], curr_routine)
                elif f == "INC":
                    curr_routine = INC(params[0], curr_routine)
                elif f == "INV":
                    curr_routine = INV(params[0], curr_routine)
                elif f == "JMP":
                    curr_routine = JMP(params[0], curr_routine)
                elif f == "JZ":
                    curr_routine = JZ(params[0], curr_routine)
        return str(u32(R[42]))

def u32(b):
    return int(b, 2)

def m32(n):
    if n > 4294967295:
        n = n % 4294967295 - 1
    if n < 0:
        n = 4294967295 + (-n) - 1 % 4294967295
    return bin(n)[2:].zfill(32)

import smtplib
# class CPUEmulator_MINE:
class CPUEmulator:
    def __init__(self):
        self.reg_dct = {}


    def run(self, subroutine):
        cmd_lst = [""]
        cmd_dct = {"MOV": self.mov,
                   "ADD": self.add,
                   "DEC": self.dec,
                   "INC": self.inc,
                   "INV": self.inv,
                   "JMP": self.jmp,
                   "JZ": self.jz}

        for i in range(43):
            if i < 10:
                self.reg_dct["R0{}".format(i)] = 0
            else:
                self.reg_dct["R{}".format(i)] = 0

        for elem in subroutine:
            lst = elem.split(" ")
            if len(lst) == 0:
                return 0
            cmd = lst[0]
            if len(lst) > 1:
                params = lst[1].split(",")
                cmd = cmd_dct[cmd]
                cmd_lst.append([cmd, params])

        i = 1
        cmd_len = len(cmd_lst)
        while i < cmd_len:
            cmd = cmd_lst[i][0]
            params = cmd_lst[i][1]
            ret = cmd(params)
            if ret:
                i = ret
            else:
                i += 1

        return str(self.reg_dct["R42"])

    def mov(self, params):
        """
        a) MOV Rxx,Ryy - copies the value from register Rxx to register Ryy
        b) MOV d,Rxx - copies the numeric constant d (specified as a decimal) to register Rxx
        """
        if len(params) < 2:
            return
        p1 = params[0]
        p2 = params[1]
        if p1.isdigit():
            self.reg_dct[p2] = int(p1)
        else:
            self.reg_dct[p2] = self.reg_dct[p1]

    def add(self, params):
        """ADD Rxx,Ryy - calculates (Rxx + Ryy) MOD 2^32 and stores the result in Rxx"""
        if len(params) < 2:
            return
        x = self.reg_dct[params[0]]
        y = self.reg_dct[params[1]]
        self.reg_dct[params[0]] = (x + y) % (2** 32)

    def dec(self, params):
        """DEC Rxx - decrements Rxx by one. Decrementing 0 causes an overflow and results in 2^(32-1)"""
        reg = params[0]
        if self.reg_dct[reg] == 0:
            self.reg_dct[reg] = (2 ** 32) - 1
        else:
            self.reg_dct[reg] -= 1

    def inc(self, params):
        """INC Rxx - increments Rxx by one. Incrementing (2^32)-1 causes an overflow and results in 0"""
        reg = params[0]
        if self.reg_dct[reg] == (2 ** 32) - 1:
            self.reg_dct[reg] = 0
        else:
            self.reg_dct[reg] += 1

    def inv(self, params):
        """INV Rxx - performs a bitwise inversion of register Rxx"""
        reg = params[0]
        self.reg_dct[reg] = ~self.reg_dct[reg]

    def jmp(self, params):
        """JMP d - unconditionally jumps to instruction number d (1-based).
        d is guaranteed to be a valid instruction number"""
        return int(params[0])

    def jz(self, params):
        """JZ d - jumps to instruction d (1-based) only if R00 contains 0"""
        if self.reg_dct["R00"] == 0:
            return int(params[0])


def cpuEmulator(subroutine):
    return CPUEmulator().run(subroutine)


def test(sol, retval):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0


test("50", cpuEmulator(["MOV 5,R00",
                        "MOV 10,R01",
                        "JZ 7",
                        "ADD R02,R01",
                        "DEC R00",
                        "JMP 3",
                        "MOV R02,R42"]))

test("2147483648", cpuEmulator(["MOV 32,R00",
                                "MOV 1,R41",
                                "JZ 8",
                                "MOV R41,R42",
                                "ADD R41,R42",
                                "DEC R00",
                                "JMP 3",
                                "NOP"]))

test("0", cpuEmulator(["MOV 32,R00",
                       "MOV 1,R41",
                       "JZ 7",
                       "ADD R41,R41",
                       "DEC R00",
                       "JMP 3",
                       "NOP",
                       "MOV R41,R42"]))

test("4294967295", cpuEmulator(["INV R41",
                                "ADD R42,R41"]))

test("4294967294", cpuEmulator(["DEC R42",
                                "INC R01",
                                "ADD R02,R01",
                                "ADD R00,R02",
                                "ADD R00,R42",
                                "JZ 1"]))

test("4294954797", cpuEmulator(["MOV 12499,R00",
                                "JZ 6",
                                "DEC R00",
                                "DEC R42",
                                "JMP 2",
                                "NOP",
                                "NOP"]))

test("4294967292", cpuEmulator(["DEC R39",
                                "DEC R39",
                                "MOV R39,R42",
                                "DEC R42",
                                "MOV 4294967295,R41",
                                "ADD R42,R41"]))

test("10100", cpuEmulator(["INV R42",
                           "MOV 101,R00",
                           "JZ 13",
                           "MOV R00,R08",
                           "MOV 100,R00",
                           "JZ 10",
                           "INC R42",
                           "DEC R00",
                           "JMP 6",
                           "MOV R08,R00",
                           "DEC R00",
                           "JMP 3",
                           "INC R42"]))

test("0", cpuEmulator(["ADD R03,R33"]))


test("0", cpuEmulator(["ADD R03,R33"]))




"""

    MOV Rxx,Ryy - copies the value from register Rxx to register Ryy;
    MOV d,Rxx - copies the numeric constant d (specified as a decimal) to register Rxx;
    ADD Rxx,Ryy - calculates (Rxx + Ryy) MOD 2^32 and stores the result in Rxx;
    DEC Rxx - decrements Rxx by one. Decrementing 0 causes an overflow and results in 232-1;
    INC Rxx - increments Rxx by one. Incrementing 232-1 causes an overflow and results in 0;
    INV Rxx - performs a bitwise inversion of register Rxx;
    JMP d - unconditionally jumps to instruction number d (1-based). d is guaranteed to be a valid instruction number;
    JZ d - jumps to instruction d (1-based) only if R00 contains 0;
    NOP - does nothing.
"""
