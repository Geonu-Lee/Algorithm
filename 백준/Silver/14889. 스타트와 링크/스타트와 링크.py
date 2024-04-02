import sys
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def cal(team_a, team_b):
    a = 0
    b = 0
    for i in range(M):
        for j in range(M):
            a += matrix[team_a[i]][team_a[j]]
            b += matrix[team_b[i]][team_b[j]]
    return abs(a-b)
def dfs(n, team_a, team_b):
    global answer
    if n == N:
        if len(team_a) == len(team_b):
            answer = min(answer, cal(team_a, team_b))
        return

    dfs(n+1, team_a + [n], team_b)
    dfs(n+1, team_a, team_b + [n])
M = N // 2
answer = 1e12
dfs(0, [], [])
print(answer)
