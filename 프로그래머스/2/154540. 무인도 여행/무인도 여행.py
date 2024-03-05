from collections import deque

def bfs(x, y, m, n, visited, maps):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = int(maps[x][y])
    while q:
        px, py = q.popleft()
        for (dx, dy) in directions:
            nx, ny = px + dx, py + dy
            if 0 <= nx < m and 0 <= ny < n \
                and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                q.append((nx, ny))
                count += int(maps[nx][ny])
                visited[nx][ny] = 1
    return count
def solution(maps):
    answer = []
    m, n = len(maps), len(maps[0])
    visited = [[0] * n for _ in range(m)]
    
    for x in range(m):
        for y in range(n):
            if maps[x][y] != "X" and visited[x][y] == 0:
                count = bfs(x, y, m, n, visited, maps)
                answer.append(count)
    
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)