from collections import deque

def solution(s):
    check = 0
    s = deque(s)
    while s:
        now = s.popleft()
        if now == "(":
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    if check == 0:
        return True
    else:
        return False