def solution(sizes):
    maxs = []
    mins = []
    for s in sizes:
        maxs.append(max(s))
        mins.append(min(s))
    w = max(maxs)
    h = max(mins)
    return w * h