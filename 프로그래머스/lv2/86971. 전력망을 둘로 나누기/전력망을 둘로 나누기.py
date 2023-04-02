from collections import deque
import copy

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = 1000
    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)
    graph = deque(graph)
    for w1, w2 in wires:
        new_graph = copy.deepcopy(graph)
        new_graph[w1].remove(w2)
        new_graph[w2].remove(w1)
        visited = [False] * (n + 1)
        c1 = bfs(new_graph, w1, visited)
        visited = [False] * (n + 1)
        c2 = bfs(new_graph, w2, visited)
        answer = min(answer, abs(c2 - c1))
    return answer