import sys
from sort.selection_sort import selection_sort

#n = int(input().strip())
unsorted = ['6',
            '31415926535897932384626433832795',
            '1',
            '3',
            '10',
            '3',
            '5',]

bucket = {}
for elem in unsorted:
    length = len(elem)
    num = elem
    if not length in bucket:
        bucket[length] = []
    bucket[length].append(num)

for key in sorted(bucket):
    for val in sorted(bucket[key]):
        print(val)
#unsorted = [int(x) for x in unsorted]
#print([str(x) for x in selection_sort(unsorted)])