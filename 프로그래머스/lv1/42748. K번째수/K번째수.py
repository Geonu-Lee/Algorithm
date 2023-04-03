def solution(array, commands):
    answer = []
    for c1, c2, c3 in commands:
        tmp = array[c1 -1: c2]
        tmp.sort()
        answer.append(tmp[c3-1])
    
    return answer