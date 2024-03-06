def solution(name, yearning, photo):
    answer = []
    d = {}
    for (n, y) in zip(name, yearning):
        d[n] = y
        
    for p in photo:
        s = 0
        for name in p:
            s += d.get(name, 0)
        answer.append(s)
        
    return answer