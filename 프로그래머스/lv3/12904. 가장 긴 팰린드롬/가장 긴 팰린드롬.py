def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        for j in range(length, i, -1):
            n_s = s[i:j]
            if n_s == n_s[::-1]:
                answer = max(answer, len(n_s))
    
    return answer