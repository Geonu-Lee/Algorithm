def solution(n, computers):
    answer = 0
    visit = [0] * n
    
    def dfs(p):
        visit[p] = 1
        for index, c in enumerate(computers[p]):
            if c and visit[index] == 0:
                dfs(index)
    for p in range(n):
        if visit[p] == 0:
            dfs(p)
            answer += 1
    return answer