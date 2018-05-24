from sgk_test import test
def mapDecoding(message):
    retval = 0
    pos = []
    stk = [([], message)]
    st = set()
    while stk:
        letters, rem = stk.pop()
        if rem == "":
            retval += 1
            pos.append(letters)
            continue
        s = ""
        i = 0
        while i < len(rem):
            s += rem[i]
            if int(s) > 26:
                break
            tup = (letters + [s], rem[i+1:])
            if tup not in st:
                stk.append((letters + [s], rem[i+1:]))
                st.add(tup)


            i += 1
    return retval





def main():
    ######### TESTS ############
    # test(3, mapDecoding("123"))
    test(5, mapDecoding("10122110"))
    # test(782204094, mapDecoding("1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211"))

if __name__ == "__main__":
    main()

