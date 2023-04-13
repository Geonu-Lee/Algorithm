def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    n = len(s)
    for i in range(1, n+1):
        new = ""
        count = 1
        tmp = s[:i]
        for j in range(i, n, i):
            if tmp == s[j:i+j]:
                count +=1
            else:
                if count != 1:
                    new = new + str(count) + tmp
                else:
                    new = new + tmp
                tmp = s[j:j+i]
                count = 1
                
        if count != 1:
            new = new + str(count) + tmp
        else:
            new = new + tmp
        
        answer.append(len(new))
    
    return min(answer)