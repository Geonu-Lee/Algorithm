def solution(survey, choices):
    answer = ''
    score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    type_str = ["RT", "CF", "JM", "AN"]
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            tmp = [3, 2, 1]
            score[s[0]] += tmp[c-1]
        elif c > 4:
            tmp = c - 4
            score[s[1]] += tmp
    for i in range(4):
        t = type_str[i]
        if score[t[0]] > score[t[1]]:
            answer += t[0]
        elif score[t[0]] < score[t[1]]:
            answer += t[1]
        elif score[t[0]] == score[t[1]]:
            answer += t[0]
            
    return answer