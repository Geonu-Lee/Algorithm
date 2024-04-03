import sys

N = input()
a_list = list(map(int, sys.stdin.readline().split()))
b, c = list(map(int, sys.stdin.readline().split()))

answer = int(N)
for a in a_list:
    tmp = a - b
    if tmp > 0:
        if tmp % c == 0:
            answer += tmp // c
        else:
            answer += (tmp // c) + 1

print(answer)