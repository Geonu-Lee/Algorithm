def solution(brown, yellow):
    case_list = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            case_list.append([i, int(yellow / i)])
            
    for v1, v2 in case_list:
        tmp = v1 * 2 + v2 * 2 + 4
        if tmp == brown:
            return [v2 + 2, v1 + 2]
    