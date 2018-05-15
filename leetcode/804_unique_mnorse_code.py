import sys
import os
from  urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
# import urllib.request
# import urllib.parse


from collections import defaultdict
class Solution:
    def uniqueMorseRepresentations(self,words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---",
                 ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alpha = [chr(x) for x in range(97, 123)]
        dct = dict(zip(alpha, morse))
        translations = set()
        for word in words:
            s = ""
            for c in word:
                trans = dct[c]
                s += trans
            if s not in translations:
                translations.add(s)
        return len(translations)



def main():
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


if __name__ == '__main__':
    main()


