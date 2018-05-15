"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0..255 (included).

Input to the function is guaranteed to be a single string.

Examples

// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
"""

class Solution():
    def is_valid_IP(self, strng):
        if strng == "":
            return False
        arr = []
        x = 0
        _len = len(strng)
        i = 0
        e = 1
        while e <= _len:
            sub = strng[i:e]
            if e < _len - 1:
                nxt = strng[e]
            else:
                nxt = None
            if e == _len or nxt == ".":
                i = e+1
                e = i + 1
                if self.is_num(sub):
                    if len(sub) > 1 and sub.startswith("0") or sub.startswith("00"):
                        return False
                    num = int(sub)
                    if num < 0 or num > 255:
                        return False
                    else:
                        arr.append(num)
                        x += 1
                else:
                    return False
            else:
                e += 1
        return False if len(arr) != 4 else True

    def is_num(self, str):
        for c in str:
            if c.isdigit() == False:
                return False
        return True


def main():
    print(Solution().is_valid_IP("12.255.56.1"))      # True
    print(Solution().is_valid_IP(""))                 # False
    print(Solution().is_valid_IP("abc.def.ghi.jkl"))  # False
    print(Solution().is_valid_IP("123.456.789.0"))    # False
    print(Solution().is_valid_IP("12.34.56"))         # False
    print(Solution().is_valid_IP("12.34.56 .1"))      # False
    print(Solution().is_valid_IP("12.34.56.-1"))      # False
    print(Solution().is_valid_IP("123.045.067.089"))  # False
    print(Solution().is_valid_IP("127.1.1.0"))        # True
    print(Solution().is_valid_IP("0.0.0.0"))          # True
    print(Solution().is_valid_IP("0.34.82.53"))       # True
    print(Solution().is_valid_IP("192.168.1.300"))    # False


if __name__ == '__main__':
    main()