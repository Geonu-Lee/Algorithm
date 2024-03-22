from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        tmp = 0
        p = q.popleft()
        for pp in q:
            tmp += 1
            if pp < p:
                break
        answer.append(tmp)
    return answer