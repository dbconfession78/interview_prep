#!/usr/bin/python3
# There is a collection of  strings ( There can be multiple occurences of
# a particular string ). Each string's length is no more than  characters.
# There are also  queries. 

# For each query, you are given a string, and you need to find out how
# many times this string occurs in the given collection of  strings.

N = 0
strings = []
queries = []

def main():
    N = int(input())
    for i in range(N):
        strings.append(input())

    Q = int(input())
    for i in range(Q):
        queries.append(input())

    for q in queries:
        print(strings.count(q))

if __name__ == '__main__':
    main()
