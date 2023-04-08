def solution(n):
    answer = 0
    for i in range(n):
        p = i + 1
        k = 0
        tmp = 0
        while tmp < n:
            tmp = tmp + (p + k)
            k += 1
            if tmp == n:
                answer +=1
        
    
    return answer