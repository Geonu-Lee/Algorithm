import heapq

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, dd in graph[now]:
            cost = dist + dd
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

def solution(n, edge):
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))
        
    dijkstra(1, graph, distance)
    
    for i, d in enumerate(distance):
        if d == INF:
            distance[i] = -1
    return distance.count(max(distance))