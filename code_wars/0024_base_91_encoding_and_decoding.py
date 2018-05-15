"""
BasE91 is a method for encoding binary as ASCII characters. It is more efficient
than Base64 and needs 91 characters to represent the encoded data.

The following ASCII charakters are used:

'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
'!#$%&()*+,./:;<=>?@[]^_`{|}~"'
Create two functions that encode strings to basE91 string and decodes the other way round.

b91encode('test') = 'fPNKd'
b91decode('fPNKd') = 'test'

b91decode('>OwJh>Io0Tv!8PE') = 'Hello World!'
b91encode('Hello World!') = '>OwJh>Io0Tv!8PE'

Input strings are valid.

"""
def b91decode(strng):
    pass


def b91encode(strng):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\""
    nums = [_ for _ in range(91)]
    # print(numpy.base_repr(ord('t'),32))

    pass


def main():
    # str = "Attack at dawn!"
    str = "test"
    # str = "green"
    # str = "foobar"
    retval = ""
    bit_len = len(str)*8
    pad = 0
    while bit_len % 6 != 0:
        pad += 1
        bit_len += 1

    x = [bin(ord(x))[2:] for x in str]
    for i, w in enumerate(x):
        lst = list(w)
        while len(lst) < 8:
            lst.insert(0, "0")
        x[i] = ''.join(lst)

    concat = list(''.join(x)) + ["0" for x in range(pad)]
    i = 0
    while i < len(concat):
        if i % 7 == 0:
            concat.insert(i, " ")
        i += 1
    concat = ''.join(concat).strip(" ")
    concat = concat.split(" ")
    for elem in concat:
        dec = bin_str_to_dec(elem)
        retval += dec_to_ascii(dec)
    _len = len(retval)
    end_pad = 0
    while _len % 4 != 0:
        end_pad += 1
        _len += 1

    retval += ("=" * (end_pad))
    print(retval)

def dec_to_ascii(dec):
    CHAR = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\""]
    # CHAR = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\""]
    # nums = [_ for _ in range(91)]

    # INT = [_ for _ in range(64)]
    retval = ""
    while dec > 91:
    # while dec > 64:
        retval += CHAR[dec % 10]
        dec //= 10
    retval += CHAR[dec]
    return retval





def bin_str_to_dec(str):
    _len = len(str)
    i = 0
    lst = [int(x) for x in list(str)]
    retval = 0
    while lst:
        retval += lst.pop() * (2**i)
        i += 1
    return retval



    # print(bit_len)


    # print(ord('y'))
    # print(ord('e'))
    # print(ord('s'))
    # print(ord('s'))
    # print(ord('i'))
    # print(ord('r'))




    print(b91decode("test"))                # "fPNKd"
    print(b91decode("Hello World!"))        # ">OwJh>Io0Tv!8PE"
    print(b91encode("fPNKd"))               # "test"
    print(b91encode(">OwJh>Io0Tv!8PE"))     # "Hello World!"





if __name__ == '__main__':
    main()
