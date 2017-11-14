#!/usr/bin/python3
def main():
    s = "ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx"
    print(super_reduced_string(s))


def super_reduced_string(s):
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    if s == '':
        return 'Empty String'
    else:
        return(s)
    

if __name__ == '__main__':
    main()
