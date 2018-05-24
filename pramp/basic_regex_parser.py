from sgk_test import test

def is_match(text, pattern):
    if text == pattern:
        return True

    def star(char, slc):
        i = 0
        retval = 0
        _len = len(slc)
        while i < _len and slc[i] == char:
            retval += 1
            i += 1
        return retval

    len_t = len(text)
    len_p = len(pattern)

    i = j = 0
    while i < len_t:
        p = pattern[j]

        if j < len_p - 1 and pattern[j + 1] == "*":
            if p == ".":
                return True
            adv = star(p, text[i:])
            i += adv
            j += 2
            continue
        elif p == ".":
            i += 1
            j += 1
            continue
        else:
            if text[i] != p:
                return False
        if j + 1 == len_p and i + 1 < len_t:
            return False

        i += 1
        j += 1
    return True


def main():
    ######### TESTS ############
    test(True, is_match("", ""))

    test(False, is_match("aa", "a"))
    test(True, is_match("aa", "aa"))
    test(True, is_match("", "a*"))
    test(False, is_match("abbdbb", "ab*d"))
    test(True, is_match("aba", "a.a"))
    test(True, is_match("acd", "ab*c."))
    test(True, is_match("abaa", "a.*a*"))

    test(True, is_match("abc", "a.c"))
    test(True, is_match("abbb", "ab*"))
    test(True, is_match("acd", "ab*c."))
    test(True, is_match("abaa", "a.*a*"))

if __name__ == "__main__":
    main()

