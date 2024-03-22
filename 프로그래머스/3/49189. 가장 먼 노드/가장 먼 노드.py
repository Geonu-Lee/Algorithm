import heapq

INF = 1e12

def dijkstra(start, graph, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # distance, now
    
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for edge, dd in graph[now]:
            cost = d + dd
            if cost < distance[edge]:
                distance[edge] = cost
                heapq.heappush(q, (cost, edge))
    return distance

def solution(n, edge):
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for e1, e2 in edge:
        graph[e1].append((e2, 1))
        graph[e2].append((e1, 1))
    distance = dijkstra(1, graph, distance)
    
    for i, d in enumerate(distance):
        if d == INF:
            distance[i] = -1
        
    return distance.count(max(distance))