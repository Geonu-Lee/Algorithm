import re
import copy
def solution(babbling):
    answer = 0
    # aya = 1, ye = 2, woo = 3, ma = 4
    for i, s in enumerate(babbling):
        babbling[i] = re.sub("aya", "1", babbling[i])
        babbling[i]= re.sub("ye", "2", babbling[i])
        babbling[i] = re.sub("woo", "3", babbling[i])
        babbling[i] = re.sub("ma", "4", babbling[i])
    for s in babbling:
        if s.isnumeric() == True:
            if "11" in s or "22" in s or "33" in s or "44" in s:
                pass
            else:
                answer += 1
    return answer