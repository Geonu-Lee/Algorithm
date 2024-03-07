from collections import Counter

def solution(topping):
    answer = 0
    young = set()
    older = Counter(topping)
    for t in topping:
        older[t] -= 1
        young.add(t)
        if older[t] == 0:
            older.pop(t)
        if len(young) == len(older):
            answer +=1
    
    return answer