from collections import defaultdict

def solution(clothes):
    dic = defaultdict(list)
    answer = 1
    for i, k in clothes:
        dic[k].append(i)
    for k in dic.keys():
        answer = answer * (len(dic[k]) + 1)
    
    return answer-1  