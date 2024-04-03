import sys
import copy

N = input()
a_list = list(map(int, sys.stdin.readline().split()))
c1, c2, c3, c4 = list(map(int, sys.stdin.readline().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈

arr = []
arr.extend(["+"] * c1)
arr.extend(["-"] * c2)
arr.extend(["x"] * c3)
arr.extend(["/"] * c4)

# 순열
visited = [0] * len(arr)
comb_list = []


def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        comb_list.append(" ".join(new_arr))
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

permutations(len(arr), [])
comb_list = list(set(comb_list))
def cal(cal_list):
    cal_list = cal_list.split(" ")
    tmp_list = copy.deepcopy(a_list)
    for i in range(len(cal_list)):
        if cal_list[i] == "+":
            tmp_list[i + 1] = tmp_list[i] + tmp_list[i+1]
        elif cal_list[i] == "-":
            tmp_list[i + 1] = tmp_list[i] - tmp_list[i+1]
        elif cal_list[i] == "x":
            tmp_list[i + 1] = tmp_list[i] * tmp_list[i + 1]
        elif cal_list[i] == "/":
            if tmp_list[i] * tmp_list[i + 1] < 0:
                if tmp_list[i] < 0:
                    tmp_list[i] = tmp_list[i] * (-1)
                elif tmp_list[i + 1] < 0:
                    tmp_list[i + 1] = tmp_list[i + 1] * (-1)
                tmp_list[i + 1] = (-1) * (tmp_list[i] // tmp_list[i + 1])
            else:
                tmp_list[i + 1] = tmp_list[i] // tmp_list[i + 1]
    return tmp_list[-1]

min_value = 1e11
max_value = -1e11

for c in comb_list:
    value = cal(c)
    min_value = min(min_value, value)
    max_value = max(max_value, value)

print(max_value)
print(min_value)


