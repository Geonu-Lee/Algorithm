from itertools import permutations

def solution(numbers):
    answer = []
    number_list = []
    for n in numbers:
        number_list.append(n)
    # print(number_list)
    length = len(numbers)
    comb_list = []
    for i in range(1, length + 1):
        tmp = list(permutations(number_list, i))
        tmp = [int("".join(t)) for t in tmp]
        comb_list.extend(tmp)
    
    for c in comb_list:
        if c < 2:
            continue
        check = True
        for i in range(2, int(c**0.5) + 1):
            if c % i == 0:
                check = False
                break
        if check: 
            answer.append(c)
    
    
    return len(set(answer))