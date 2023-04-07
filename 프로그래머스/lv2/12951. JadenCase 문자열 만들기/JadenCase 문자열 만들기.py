def solution(s):
    s = s.split(" ")
    answer = []
    for i in range(len(s)):
        if s[i] == '':
            pass
        elif s[i][0].islower():
            s[i] = s[i][0].upper() + s[i][1:].lower()
        else:
            s[i] = s[i][0] + s[i][1:].lower()
        answer.append(s[i])
        
    return " ".join(s_ for s_ in s)

