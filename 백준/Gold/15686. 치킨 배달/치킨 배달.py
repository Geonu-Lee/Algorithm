import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def get_distance(house_list, chicken_list):
    total_distance = 0
    for house in house_list:
        house_distance = 1e09
        for chicken in chicken_list:
            distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            house_distance = min(house_distance, distance)
        total_distance += house_distance
    return total_distance

# 치킨집 찾기
chicken_list = []
house_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken_list.append((i + 1, j + 1))
        elif arr[i][j] == 1:
            house_list.append((i + 1, j + 1))

answer = 1e09
if len(chicken_list) == M:  # 이미 M 이랑 치킨집 개수랑 같을 때
    answer = get_distance(house_list, chicken_list)
else:
    chosen_list = []
    def combinations(n, new_arr, c):
        if len(new_arr) == n:
            chosen_list.append(new_arr)
            return
        for i in range(c, len(chicken_list)):
            combinations(n, new_arr + [chicken_list[i]], i + 1)
    combinations(M, [], 0)
    for chosen in chosen_list:
        tmp = get_distance(house_list, chosen)
        answer = min(answer, tmp)
print(answer)
