#!/usr/bin/python3

def main():
    strs = ["StuartA", "StufartB", "StusmartC", "StudyartD", "StudenttartE", "StupiddartF"]
    print(longest_common_prefix(strs))

def longest_common_prefix(strs):
    common = ''
    i = 0
    if len(strs) == 0:
        return common

    short_len = min([len(s) for s in strs])
    while i < short_len:
        win = strs[0][:i+1]
        if not all([s.startswith(win) for s in strs]):
            break;
        common = win
        i += 1
    return common



if __name__ == '__main__':
    main()
