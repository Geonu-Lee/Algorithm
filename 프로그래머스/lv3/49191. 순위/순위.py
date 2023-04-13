from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    for w, l in results:
        win[l].add(w)  # 00 한테 이긴 선수들
        lose[w].add(l) # 00 한테 진 선수들
    for i in range(1, n+1):
        for w in win[i]:
            lose[w].update(lose[i])    
        for l in lose[i]:
            win[l].update(win[i])
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer