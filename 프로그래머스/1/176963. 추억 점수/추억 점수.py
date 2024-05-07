def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]

    for p in photo:
        tmp = 0
        for pp in p:
            tmp += score.get(pp, 0)
        answer.append(tmp)
        
    return answer