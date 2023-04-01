def solution(s):
    answer = []
    check = {}
    for i in range(len(s)):
        tmp = check.get(s[i], -1)
        if tmp == -1:
            answer.append(-1)
        else:
            answer.append(i - check[s[i]])
        check[s[i]] = i
            
    return answer