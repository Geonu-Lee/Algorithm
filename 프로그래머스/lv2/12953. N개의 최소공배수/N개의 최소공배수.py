import math

def lcm(x, y):
    return x * y // math.gcd(x,y)

def solution(arr):
    answer = 0
    for i in range(1, len(arr)):
        if i == 1:
            answer = lcm(arr[i-1], arr[i])
        else:
            answer = lcm(answer, arr[i])
    return answer