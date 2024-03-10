def solution(N, number):
    answer = 0
    num_list = []
    for i in range(1,9):
        tmp = set()
        tmp.add(int(str(N) * i))
        for j in range(i-1):
            for x in num_list[j]:
                for y in num_list[-j-1]:
                    tmp.add(x+y)
                    tmp.add(x-y)
                    tmp.add(x*y)
                    if not y == 0:
                        tmp.add(x//y)
        if number in tmp:
            return i
        else:
            num_list.append(tmp)
    return -1