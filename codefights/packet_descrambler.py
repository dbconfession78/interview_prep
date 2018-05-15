"""
SpaceX has built a reliable Earth-Mars communication system that uses n links to transmit messages that are broken into fragments. The messages are sequences of ASCII characters that terminate with '#'. n copies of each fragment are sent, meaning that normally n copies of each fragment are received (one per link). However, some fragments may be lost. It's also possible that they can be corrupted or arrive out of order.

Each fragment contains the following data:

    seq - The sequential number of the fragment in the message. This part of the fragment is never corrupted.
    fragmentData - A single character from the message contained in the fragment.

Implement a function that receives an array of message fragments and reconstructs the original message according to the following rules:

    For each sequential number, pick the data character that is present in more than 50% of the fragments with that sequential number. Note that we calculate 50% based on the total number of copies that were sent (which is always equal to n), while the number of received fragments can be smaller.
    The last fragment of the message that's been reconstructed according to rule 1 (and no other fragment) contains '#'.
    There can be no gaps in the message, so all of the fragments numbered 0, 1, 2, ..., <number of the last fragment> should be restored.

If the message cannot be reconstructed, return an empty string. Otherwise, return the reconstructed message.

Example

For seq = [1, 1, 0, 0, 0, 2, 2, 2], fragmentData = ['+', '+', 'A', 'A', 'B', '#', '#', '#'], and n = 3, the output should be
packetDescrambler(seq, fragmentData, n) = "A+#".

    For the fragment with index 0 (sequential number), 2 'A's and 1 'B' were received. So, the number of fragments with 'A' is more than 50% out of n = 3. Both parts of rule 1 hold, meaning that the initial character of the message is 'A'.
    For the fragment with index 1 (sequential number), 2 '+'s were received and the third fragment was lost. Again, the number of fragments with '+' is more than 50% out of n = 3. Therefore, the next character of the message is '+'.
    For the fragment with index 2 (sequential number), 3 '#'s were received. All the sent fragments agree, so rule 1 holds. There are no fragments with a sequential number of more than 2, meaning that this is the last character. Since this character is '#', rule 2 holds as well.
    Note that there were no gaps before '#', so rule 3 holds. Hence, the message can be considered correctly reconstructed.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer seq

    An array of non-negative integers. seq[i] contains the sequential number of the ith received fragment.

    Guaranteed constraints:
    1 ≤ seq.length ≤ 105,
    0 ≤ seq[i] < 25000.

    [input] array.char fragmentData

    An array of characters. fragmentData[i] contains a printable ASCII character transmitted in the ith received fragment.

    Guaranteed constraints:
    fragmentData.length = seq.length.

    [input] integer n

    The number of links (in other words, the number of copies of the message that were sent).

    Guaranteed constraints:
    3 ≤ n ≤ 25000.

    [output] string

    Return the reconstructed message. If the message can't be reconstructed correctly, return an empty string.

"""
from collections import defaultdict, Counter


def packetDescrambler(seq, fragmentData, n):
    s = set()
    seq_dct = defaultdict(list)
    retval = ""
    info = []

    for i, elem in enumerate(seq):
        seq_dct[elem].append(fragmentData[i])
    for k, v in seq_dct.items():
        tmp_dct = {}
        counts = Counter(v)
        for K, V in counts.items():
            tmp_dct[K] = V / n
        percents = [K for K, V in tmp_dct.items() if V > 0.5]
        if not percents:
            return retval
        seq_dct[k] = percents[0]

    for k, v in seq_dct.items():
        info.append({"seq": k, "frag": v})
    info = sorted(info, key=lambda k: k["seq"])
    for i, elem in enumerate(info):
        if i > 1:
            if elem["seq"] != info[i-1]["seq"] + 1:
                return ""
        if elem["frag"] == "#":
            if "#" in s:
                return ""
            s.add("#")
        retval += elem["frag"]
    if retval[-1] != "#":
        return ""
    return retval


# "A+#"
print(packetDescrambler([1, 1, 0, 0, 0, 2, 2, 2],  ["+",
 "+",
 "A",
 "A",
 "B",
 "#",
 "#",
 "#"], 3))

# ""
print(packetDescrambler([1, 1, 0, 0, 0, 2, 2, 2], ["+",
 "+",
 "A",
 "A",
 "B",
 "#",
 "#",
 "#"], 4))

# ""
print(packetDescrambler([1, 1, 2, 2, 2, 0, 0, 0], ["+",
 "+",
 "A",
 "A",
 "B",
 "#",
 "#",
 "#"], 3))

# ""
print(packetDescrambler([1, 1, 2, 2, 2, 0, 0, 0, 4, 4], ["+",
 "+",
 "A",
 "A",
 "B",
 "#",
 "#",
 "#",
 "#",
 "#"], 3))

# ""
print(packetDescrambler([1, 1, 2, 2, 2, 4, 4], ["+",
 "+",
 "A",
 "A",
 "B",
 "#",
 "#"], 3))

