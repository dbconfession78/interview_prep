"""
Esoteric languages are pretty hard to program, but it's fairly interesting to write interpreters for them!

Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 supports the following instructions (from Wikipedia):

0-9 Push this number onto the stack.
+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.


! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.


> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.

" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.

\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.

$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
<space> No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.

Here's an example:

>987v>.v
v456<  :
>321 ^ _@
will create the output 123456789.

So what you must do is create a function such that when you pass in the Befunge code, the function returns the output that would be generated by the code. So, for example:

"123456789".equals(new BefungeInterpreter().interpret(">987v>.v\nv456<  :\n>321 ^ _@")

"""
import random


def interpret(code):
    b = Befunge(code)
    dct = {
        "!": b.logical_not, "`": b.greater_than,
        "+": b.add, "-": b.sub, "*": b.mul, "/": b.div, "%": b.mod,
        "_": b.pop_and_turn_h, "|": b.pop_and_turn_v, "$": b.pop_and_throw,
        "\"": b.string_mode, ":": b.dupe_stk_top, "\\": b.swap_top_two, ".": b.write_as_int, ",": b.write_as_ascii,
        "#": b.move,
        "p": b.put, "g": b.get,
        "@": b.end_program
    }
    while not b.done:
        c = b.read()
        if c in "><^v?":
            b.set_dir(c)
        elif c.isdigit():
            b.stk.append(int(c))
        else:
            fn = dct.get(c)
            if fn:
                fn()
    return b.output


class Befunge:
    def __init__(self, code):
        self.nl_lst = [i for (i, x) in enumerate(code) if x == "\n"]
        if "@\n" in code:
            code = code.replace("@\n", "@")

        self.stk = []
        self.direction = "right"
        self.code = code
        self.code_list = [list(x) for x in self.code.split("\n")]
        self.pos = -1
        self._len = len(code)
        if "\n" not in code:
            self.row_len = self._len
        else:
            self.row_len = len(code[:code.index("\n")]) + 1
        self.dir_dct = {"right": 1, "left": -1, "up": -self.row_len, "down": self.row_len}
        self.row_count = len(self.nl_lst)+1
        self.output = ""
        self.done = False

    def has_next(self):
        return self.pos+self.dir_dct[self.direction] < self._len

    def get_next(self):
        if self.has_next():
            return self.code[self.pos+self.dir_dct[self.direction]]

    def read(self, reading_string=False):
        self.move()
        if not reading_string:
            while self.has_next() and self.pos < self._len-1 and self.code[self.pos] == " ":
                self.move()
        return self.code[self.pos]

    def set_dir(self, _dir):
        dct = {">": "right", "<": "left", "^": "up", "v": "down"}
        self.direction = random.choice([v for v in dct.values()]) if _dir == "?" else dct[_dir]

    def add(self):
        self.stk.append(self.stk.pop() + self.stk.pop())

    def sub(self):
        a = int(self.stk.pop())
        b = int(self.stk.pop())
        self.stk.append(b-a)

    def mul(self):
        self.stk.append(self.stk.pop() * self.stk.pop())

    def div(self):
        self.stk.append([0 if a == 0 else b // a for a, b in {self.stk.pop(): self.stk.pop()}.items()][0])

    def mod(self):
        self.stk.append([0 if a == 0 else b % a for a, b in {self.stk.pop(): self.stk.pop()}.items()][0])

    def logical_not(self):
        self.stk.append(1 if self.stk.pop() == 0 else 0)

    def greater_than(self):
        a = int(self.stk.pop())
        b = int(self.stk.pop())
        self.stk.append(1 if b > a else 0)

    def pop_and_turn_h(self):
        self.direction = "right" if self.stk.pop() == 0 else "left"

    def pop_and_turn_v(self):
        self.direction = "down" if self.stk.pop() == 0 else "up"

    def string_mode(self):
        while self.has_next() and self.get_next() != "\"":
            self.stk.append(ord(self.read(reading_string=True)))
        self.move()

    def dupe_stk_top(self):
        self.stk.append(self.stk[-1] if self.stk else 0)

    def swap_top_two(self):
        self.stk.insert(len(self.stk), self.stk.pop(-2) if len(self.stk) > 1 else 0)

    def pop_and_throw(self):
        self.stk.pop()

    def write_as_int(self):
        self.output += str(int(self.stk.pop()))

    def write_as_ascii(self):
        self.output += chr(self.stk.pop())

    def put(self):
        x, y, v = self.stk.pop(), self.stk.pop(), self.stk.pop()
        self.code_list[x][y] = chr(v)

    def get(self):
        x, y = self.stk.pop(), self.stk.pop()
        val = self.code_list[x][y]
        self.stk.append(ord(val))

    def move(self):
        self.pos = self.pos + self.dir_dct[self.direction]

    def end_program(self):
        self.done = True


def main():
    print(interpret(">987v>.v\n"
                    "v456<  :\n"
                    ">321 ^ _@"))                                   # "123456789"

    print(interpret(">25*\"!dlroW olleH\":v\n"
                    "                v:,_@\n"
                    "                >  ^"))                        # "Hello World!\n"

    print(interpret("08>:1-:v v *_$.@ \n"
                    "  ^    _$>\:^"))                               # '40320'

    print(interpret("01->1# +# :# 0# g# ,"
                    "# :# 5# 8# *# 4# +# -# _@"))                   # "01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"

    print(interpret("2>:3g\" \"-!v\  g30          <\n"
                    " |!`\"&\":+1_:.:03p>03g+:\"&\"`|\n"
                    " @               ^  p3\\\" \":<\n"
                    "2 2345678901234567890123456789012345678"))     # '23571113171923293137'


if __name__ == '__main__':
    main()