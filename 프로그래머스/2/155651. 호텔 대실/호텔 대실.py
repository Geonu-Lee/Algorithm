def solution(book_time):
    answer = 0
    book_time = sorted(book_time, key = lambda x:x[0])
    room = [[] for _ in range(len(book_time))]
    for i in range(len(book_time)):
        start, end = book_time[i]
        start = start.split(":")
        start = int(start[0]) * 60 + int(start[1])
        end = end.split(":")
        end = int(end[0]) * 60 + int(end[1])
        book_time[i] = [start, end]
    for book in book_time:
        for r in room:
            if len(r) == 0: # 빈방
                r.append(book)
                break
            elif r[-1][0] <= book[0] < r[-1][1] + 10:
                continue
            else:
                r.append(book)
                break
    for r in room:
        if len(r) != 0:
            answer += 1
    return answer