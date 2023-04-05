def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        tmp = max(i // n, i % n) + 1
        answer.append(tmp)
    
    return answer