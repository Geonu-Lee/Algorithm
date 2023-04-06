def solution(tickets):
    answer = []
    routes = {}
    for t1, t2 in tickets:
        if routes.get(t1, -1) == -1:
            routes[t1] = [t2]
        else:
            routes[t1].append(t2)
    for k in routes.keys():
        routes[k].sort(reverse=True)
    
    start = ["ICN"]
    while start:
        now = start[-1]
        if routes.get(now, -1) == -1 or len(routes[now]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[now].pop())
        
    return answer[::-1]