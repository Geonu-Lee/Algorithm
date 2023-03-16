import heapq

INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    
    for f in fares:
        graph[f[0]].append((f[1], f[2]))
        graph[f[1]].append((f[0], f[2]))
        
    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        return distance
    share_d = dijkstra(s)
    a_d = dijkstra(a)
    b_d = dijkstra(b)
    answer = INF
    for i in range(1, (n+1)):  # 임의의 중간지점을 선택하고 최소 경로 찾기
        answer = min(answer, share_d[i] + a_d[i] + b_d[i])
    
    return answer