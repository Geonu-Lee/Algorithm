def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            answer.add(numbers[i] + numbers[j + i + 1])
    return sorted(answer)