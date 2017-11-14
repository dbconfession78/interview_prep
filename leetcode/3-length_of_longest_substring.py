#!/usr/bin/python3

def main():

#    print(lengthOfLongestSubstring("abcabcbb"))
#    print(lengthOfLongestSubstring("bbbbb"))
#    print(lengthOfLongestSubstring("pwwkew"))
#    print(lengthOfLongestSubstring("c"))
#    print(lengthOfLongestSubstring("au"))
#    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring("tmmzuxt"))

def lengthOfLongestSubstring(s):
    window = set()
    start = end  = 0
    retval = 0

    while start < len(s) and end < len(s):
        #    while chars are uniqe, continue expanding window by 1.
        if s[end] not in window:
            window.add(s[end])
            end += 1
            retval = max(retval, end - start)
        #    if char repeats, slide window right by one (don't expand)
        else:
            window.remove(s[start])
            start += 1
    return retval

def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    max = 0
    length = 0
    i = 0
    x = 0
    sub = None

    if all(x==s[0] for x in s):
        return 1

    if len(s) <= 1:
        return len(s)
    while i < len(s)+1:
        sub = s[x:i+1]
        for c in sub:
            count = sub.count(c)
            if count > 1:
                length = len(sub)-1
                x += 1; i = x;
                if length > max:
                    max = length
                break
        i += 1

    length = len(sub)
    if max == 0:
        max = len(s)
    if length > max:
        max = length
    return(max)




if __name__ == '__main__':
        main()
