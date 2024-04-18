import math

def solution(n,a,b):
    answer = 0
    
    while True:
        next_a = math.ceil(a / 2)
        next_b = math.ceil(b / 2)
        answer += 1
        if next_a == next_b:
            return answer
        a, b = next_a, next_b