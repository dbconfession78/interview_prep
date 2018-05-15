"""
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order
to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance
between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer
"""

# def deletion_distance_PRaCTICE(str1, str2):
def deletion_distance(str1, str2):
    return


def deletion_distance_PASSED(str1, str2):
# def deletion_distance(str1, str2):
    matrix = []
    matrix.append([x for x in range(len(str2)+1)])
    for i in range(1, len(str1)+1):
        matrix.append([i])
    for i, c1 in enumerate(str1):
        for j, c2 in enumerate(str2):
            if c1 != c2:
                up = matrix[i][j+1]
                left = matrix[i+1][j]
                mn = min(up, left)
                matrix[i+1].append(mn + 1)
            else:
                matrix[i+1].append(matrix[i][j])
    return matrix[-1][-1]

print(deletion_distance("dog", "frog"))
