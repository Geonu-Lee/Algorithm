
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda a: a*3)
    return str(int("".join(x for x in numbers)))