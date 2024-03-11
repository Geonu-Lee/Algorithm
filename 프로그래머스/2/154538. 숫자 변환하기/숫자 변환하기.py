from collections import deque


def solution(x, y, n):
    answer = 0
    if x == y:
        return 0
    q = deque()
    d = [0] * (y+1)
    q.append(x)
    while q:
        px = q.popleft()
        for i in range(3):
            if i == 0:
                nx = px + n
            elif i == 1:
                nx = px * 2
            elif i == 2:
                nx = px * 3
            if nx == y:
                return d[px] + 1
            if nx < y and d[nx] == 0:
                q.append(nx)
                d[nx] = d[px] + 1
    return -1