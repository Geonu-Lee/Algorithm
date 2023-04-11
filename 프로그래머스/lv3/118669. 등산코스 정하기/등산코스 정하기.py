import heapq


def solution(n, paths, gates, summits):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    
    graph = [[] for _ in range(n+1)]
    for p in paths:
        graph[p[0]].append((p[1], p[2]))
        graph[p[1]].append((p[0], p[2]))
        
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))
        distance[gate] = 0
    
    summit = [False] * (n+1)
    for s in summits:
        summit[s] = True
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist or summit[now]:
            continue
        for g in graph[now]:
            cost = max(distance[now], g[1])
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))
    answer = [0, INF]
    for s in sorted(summits):
        if distance[s] < answer[1]:
            answer[0] = s
            answer[1] = distance[s]
    
    return answer