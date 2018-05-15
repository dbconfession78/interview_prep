"""
Smallest Substring of All Characters

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that
 finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a
  substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

Constraints:
    [time limit] 5000ms
    [input] array.character arr
        1 ≤ arr.length ≤ 30
    [input] string str
        1 ≤ str.length ≤ 500
    [output] string


"""
from collections import Counter
from collections import defaultdict
test_no = 1
class Solution():
    # def get_shortest_unique_substring_PRACTICE(self, arr, str):
    def get_shortest_unique_substring(self, arr, str):
        arr_len = len(arr)
        str_len = len(str)

        st = set(arr)
        dct = {}
        stk = []
        start = 0
        lo = float('inf')
        retval = ""
        first_match_found = False
        for i, elem in enumerate(str):
            if elem in st:
                dct[elem] = i

                if not first_match_found:
                    if len(dct) == arr_len:
                        first_match_found = True
                        retval = str[start:i+1]
                        lo = len(retval)
                else:
                    s = min(dct.values())
                    e = max(dct.values()) + 1
                    if (e - s) < lo:
                        lo = e - s
                        retval = str[s:e]
        return retval



    def get_shortest_unique_substring_MINE_PASSED(self, arr, str):
    # def get_shortest_unique_substring(self, arr, str):

        """
        :desc: 1. adv 'tail' through 'str', deleting matching elems from 'dct' until 'dct' empty.
               2. then adv 'head' through 'str' until an 'arr' elem is not in 'win'.
        :return: shortest substring with all elems from dct
        """
        dct = Counter(arr)
        str_len = len(str)
        head = 0
        retval = ""

        """ 1 """
        for tail in range(str_len):
            win = str[head:tail+1]
            if str[tail] in dct:
                del(dct[str[tail]])

                """ 2 """
                if not dct:
                    while not dct:
                        if retval == "" or len(retval) > len(win):
                            retval = win
                        head += 1
                        win = str[head:tail+1]
                        dct = Counter(arr) - Counter(str[head:tail+1])
        return retval

    def get_shortest_unique_substring_SOL(self, arr, str):
    # def get_shortest_unique_substring(self, arr, str):
        head_index = 0
        result = ""
        unique_counter = 0
        count_map = {}

        # initialize count_map
        for i in range(len(arr)):
            count_map[arr[i]] = 0

        # scan str
        for tail_index in range(len(str)):
            # handle the new tail
            tail_char = str[tail_index]

            # skip all the characters not in arr
            if str[tail_index] not in count_map:
                continue

            tail_count = count_map[tail_char]
            if tail_count == 0:
                unique_counter = unique_counter + 1

            count_map[tail_char] = tail_count + 1

            # push head forward
            while unique_counter == len(arr):
                tmp_len = tail_index - head_index + 1
                if tmp_len == len(arr):
                    # return a substring of str from
                    # head_index to tail_index (inclusive)
                    return str[head_index:tail_index]

                if result == "" or tmp_len < len(result):
                    # return a substring of str from
                    # head_index to tail_index (inclusive)
                    result = str[head_index:tail_index+1]

                head_char = str[head_index]
                if head_char in count_map:
                    head_count = count_map[head_char] - 1
                    if head_count == 0:
                        unique_counter = unique_counter - 1
                    count_map[head_char] = head_count

                head_index = head_index + 1

        return result

def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))

def main():
    test("", Solution().get_shortest_unique_substring(['A'], ''))  # ""
    test("", Solution().get_shortest_unique_substring(['A'], 'B'))  # ""
    test("A", Solution().get_shortest_unique_substring(['A'], 'A'))  # "A"
    test("BANC", Solution().get_shortest_unique_substring(["A","B","C"],"ADOBECODEBANCDDD"))   # "BANC"
    test("KADOBECODEBANCDDDEI", Solution().get_shortest_unique_substring(["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI"))
    test("zyx", Solution().get_shortest_unique_substring(['x', 'y', 'z'], 'xyyzyzyx'))  # "zyx" <-- Example
    test("", Solution().get_shortest_unique_substring(["x","y","z","r"], "xyyzyzyx"))  # ""


if __name__ == '__main__':
    main()