from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    cnt = sorted(cnt.items(), reverse=True, key = lambda x: x[1])
    for c in cnt:
        k = k - c[1]
        answer += 1
        if k <= 0:
            break
    return answer