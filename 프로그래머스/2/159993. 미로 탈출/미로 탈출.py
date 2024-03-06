from collections import deque

def bfs(x, y, n, m, visited, maps, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 1
    while q:
        x, y, t = q.popleft()
        if maps[x][y] == end:
            return t
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                q.append((nx, ny, t + 1))
                visited[nx][ny] = 1
    return -1
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if maps[x][y] == "S":
                sx, sy = x, y
            elif maps[x][y] == "L":
                lx, ly = x, y
    
    s_2_l = bfs(sx, sy, n, m, visited, maps, "L")  # S -> L
    if s_2_l == -1:
        return -1
    else:
        visited = [[0] * m for _ in range(n)]
        l_2_e = bfs(lx, ly, n, m, visited, maps, "E")  # L -> E
        if l_2_e == -1:
            return -1
        return s_2_l + l_2_e