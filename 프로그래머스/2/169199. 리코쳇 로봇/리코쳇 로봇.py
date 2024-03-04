from collections import deque

def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                q.append((x, y, 0))
    while q:
        x, y, l = q.popleft()
        if board[x][y] == "G":
            return l
        for (dx, dy) in d:
            step = 1
            while True: # 미끌어지기
                new_x, new_y = x + dx * step, y + dy * step
                if new_x < 0 or new_x >= n or new_y <0 or new_y >= m or board[new_x][new_y] == "D":
                    if not visited[new_x - dx][new_y - dy]:
                        q.append((new_x - dx, new_y - dy, l+1))
                        visited[new_x - dx][new_y - dy] = 1
                    break
                step += 1
    return -1