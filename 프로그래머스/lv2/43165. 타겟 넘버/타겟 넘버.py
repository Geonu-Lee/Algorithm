def solution(numbers, target):
    answer = 0
    leaves = [0]
    for n in numbers:
        tmp = []
        for l in leaves:
            tmp.append(l + n)
            tmp.append(l - n)
            leaves = tmp
    for l in leaves:
        if l == target:
            answer += 1
    
    return answer