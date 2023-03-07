
def solution(s):
    answer = 0
    check = ["", 0, 0]
    for t in s:
        if check[0] == "":
            check[0] = t
            check[1] += 1
        else:
            if check[0] == t:
                check[1] += 1
            else:
                check[2] += 1
            if check[1] == check[2]:
                answer += 1
                check = ["", 0, 0]
    if check != ["", 0, 0]:
        answer += 1
        
    return answer