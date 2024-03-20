from collections import deque

def bfs(x, y, n, m, visited, maps):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = 1
    
    while q:
        nx, ny, move = q.popleft()
        if nx == n-1 and ny == m-1:
            return move
        for d in directions:
            dx, dy = nx + d[0], ny + d[1]
            if 0 <= dx < n and 0<= dy < m and visited[dx][dy] == 0 and maps[dx][dy] == 1:
                q.append((dx, dy, move + 1))
                visited[dx][dy] = 1
    return -1
    
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    answer = bfs(0, 0, n, m, visited, maps)
    
    return answer