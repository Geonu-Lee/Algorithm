import sys


arr = [str(sys.stdin.readline()[:-1]) for _ in range(4)]
K = int(sys.stdin.readline())
rotate_list = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
arr = [0] + arr
def rotate(array, d):
    if d == 1:
        array = array[-1] + array[:-1]
    else:
        array = array[1:] + array[0]
    return array

for target, d in rotate_list:  # target 톱니바퀴, 방향
    check_list = [0] * 5
    check_list[target] = d
    # 타켓 톱니바퀴 오른쪽
    d_right = d
    d_left = d
    for i in range(target, 4):
        if arr[i][2] != arr[i + 1][6]:
            check_list[i + 1] = (-1) * d_right
            d_right = d_right * (-1)
        else:
            break
    # 타켓 톱니바퀴 왼쪽
    for i in range(target-1, 0, -1):
        if arr[i][2] != arr[i + 1][6]:
            check_list[i] = (-1) * d_left
            d_left = d_left * (-1)
        else:
            break

    for i in range(1, 5):
        if check_list[i] != 0:
            arr[i] = rotate(arr[i], check_list[i])

answer = 0
score_list = [0, 1, 2, 4, 8]
for i in range(1, 5):
    if arr[i][0] == "1":
        answer += score_list[i]
# if arr[1][0] == "1":
#     answer += 2
# if arr[2][0] == "1":
#     answer += 4
# if arr[3][0] == "1":
#     answer += 8

print(answer)
