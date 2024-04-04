import sys


N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direction = {
    0: (-1, 0),  # 북
    1: (0, 1),   # 동
    2: (1, 0),   # 남
    3: (0, -1)   # 서
}

back_direction = {
    0: (1, 0),  # 북
    1: (0, -1),   # 동
    2: (-1, 0),   # 남
    3: (0, 1)   # 서
}

nx = r
ny = c
answer = 0
while True:
    # print(nx, ny)
    # print(d)
    # print("---")
    if arr[nx][ny] == 0:
        answer += 1
        arr[nx][ny] = 2  # 청소 완료

    check = 0
    check_d = -1
    for key, value in direction.items():
        if arr[nx + value[0]][ny + value[1]] == 0:
            check = 1
            check_d = key
    if check == 0:  # 주위에 청소되지 않은 빈칸이 없는 경우
        bx, by = back_direction[d]
        dx, dy = nx + bx, ny + by
        if (0 <= dx < N and 0 <= dy < M and arr[dx][dy] == 1) or (M <= dx < 0 and N <= dy < 0):
            break
        nx, ny = dx, dy
    else:  # 주위에 청소되지 않은 빈칸이 있는 경우
        if d == 0:
            d = 3
        else:
            d -= 1
        fx, fy = direction[d]
        dx, dy = nx + fx, ny + fy
        if arr[dx][dy] == 0:
            nx, ny = dx, dy

print(answer)
