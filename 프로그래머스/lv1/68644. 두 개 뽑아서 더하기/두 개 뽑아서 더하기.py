def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            answer.append(numbers[i] + numbers[j + i + 1])
    answer = list(set(answer))
    answer.sort()
    return answer