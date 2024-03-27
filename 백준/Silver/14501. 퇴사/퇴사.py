import sys
N = int(input())
schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N):  # 첫번째 날부터 퇴사 전날까지
    for j in range(i+schedule[i][0], N+1):  # 해당 날짜에 상담했을 경우 가능한 날짜
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
print(dp[-1])