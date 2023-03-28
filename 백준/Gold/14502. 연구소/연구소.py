import sys; input = sys.stdin.readline
from itertools import combinations
import copy


n, m = list(map(int, input().split(" ")))  # n 세로 m 가로
map_list = []
empty_list = []
virus_list = []# 벽을 세울 수 있는 공간
for i in range(n):
    tmp = list(map(int, input().split(" ")))
    map_list.append(tmp)

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            empty_list.append([i, j])
        elif map_list[i][j] == 2:
            virus_list.append([i, j])

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

comb_list = combinations(empty_list, 3)
answer = 0
for comb in comb_list:
    new_map = copy.deepcopy(map_list)
    for x, y in comb:
        new_map[x][y] = 1
    virus = copy.deepcopy(virus_list)
    while virus:
        x_v, y_v = virus.pop()
        for x_d, y_d in direction:
            nx = x_v + x_d
            ny = y_v + y_d
            if nx >= 0 and nx < n and ny >= 0 and ny < m and new_map[nx][ny] == 0:
                new_map[nx][ny] = 2
                virus.append([nx, ny])
    count = 0
    for r in new_map:
        count += r.count(0)
    answer = max(answer, count)

print(answer)