def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)  # 기본적으로 -1로 초기화된 리스트
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer