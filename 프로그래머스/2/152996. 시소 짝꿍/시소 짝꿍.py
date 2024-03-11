from collections import Counter

def solution(weights):
    answer = 0
    count_dict = Counter(weights)
    for k, v in count_dict.items():
        if v >= 2:
            answer += v * (v-1) // 2
    weights = set(weights)
    for w in weights:
        if w * (2/3) in weights:
            answer+= count_dict[w * (2/3)] * count_dict[w]
        if w * (2/4) in weights:
            answer+= count_dict[w * (2/4)] * count_dict[w]
        if w * (3/4) in weights:
            answer+= count_dict[w * (3/4)] * count_dict[w]
    return answer


