import heapq

INF = int(1e9)

def solution(N, road, K):
    distance = [INF] * (N+1)  # for index 1
    answer = 0
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))   # distance, node
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:   # check visited
                continue
            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
    dijkstra(1)
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer