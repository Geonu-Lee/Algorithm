def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)):
        tmp = t[i:l+i]
        if int(tmp) <= int(p) and len(tmp) == l:
            answer += 1
    return answer