import math
def solution(fees, records):
    time_list = []
    number_list = []
    charge = {}
    for s in records:
        t, n, e = s.split(" ")   # 시간, 자동차 번호, 입장 여부
        if len(e) == 2:
            time_list.append(t)
            number_list.append(n)
        else:
            i = number_list.index(n)
            p_h, p_m = list(map(int, time_list[i].split(":")))
            n_h, n_m = list(map(int, t.split(":")))
            t_m = (n_h - p_h) * 60 + (n_m - p_m)
            if n in charge:
                charge[n] += t_m
            else:
                charge[n] = t_m
            time_list.pop(i)
            number_list.pop(i)
    if len(number_list) != 0:
        for i, n in enumerate(number_list):
            h, m = list(map(int, time_list[i].split(":")))
            t_m = (23 - h) * 60 + (59 - m)
            if n in charge:
                charge[n] += t_m
            else:
                charge[n] = t_m
    charge = dict(sorted(charge.items()))
    charge = list(charge.values())
    charge = [fees[1] + math.ceil((c - fees[0])/fees[2]) * fees[3] if c > fees[0] else fees[1] for c in charge ]

    
    return charge