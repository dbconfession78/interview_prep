#!/usr/bin/python3
def main():
    _input = input().strip()
    _input = _input.split(' ')
    N = int(_input[0])
    Q = int(_input[1])
    queries = []
    for i in range(Q):
        queries.append([int(n) for n in input().split(' ')])

    seq_list = [[] for i in range(N)]
    last_answer = 0
    for query in queries:
        q = query[0]
        x = query[1]
        y = query[2]
        if (q == 1):
            index = ((x ^ last_answer) % N)
            seq_list[index].append(y)
        elif (q == 2):
            index = ((x ^ last_answer) % N)
            seq = seq_list[index]
            size = len(seq)
            last_answer = seq[y % size]
            print(last_answer)
        else:
            print('Error: please choose query type 1 or 2')
            return None


if __name__ == '__main__':
    main()
