from collections import deque

def convert_time(time):
    time = time.split(":")
    time = 60 * int(time[0]) + int(time[1])
    return time

def solution(plans):
    answer = []
    p = []
    remain = []
    for (name, start, time) in plans:
        p.append([name, convert_time(start), int(time)])
    p = sorted(p, key = lambda x: x[1])
    for i in range(len(p)):
        if i == len(p)-1: # 마지막 과제에 도달했을 경우
            answer.append(p[i][0])
            for i in range(1, len(remain) + 1):
                answer.append(remain[-i][0])
            break
        gap = p[i+1][1] - (p[i][1] + p[i][2])
        if gap >=0:
            answer.append(p[i][0])
            while remain:
                if remain[-1][1] <= gap:
                    r = remain.pop()
                    answer.append(r[0])
                    gap -= r[1]
                else:
                    remain[-1][1] -= gap
                    break
        else:
            remain.append([p[i][0], -gap])
    
    return answer