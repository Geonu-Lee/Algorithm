import heapq
INF = int(1e9)

def dijkstra(start, graph, distances):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if cost < distances[g[0]]:
                distances[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))
    return distances
def solution(N, road, K):
    answer = 0
    distances = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    
    distances = dijkstra(1, graph, distances)
    for i in range(1, N+1):
        if distances[i] <= K:
            answer += 1

    return answer