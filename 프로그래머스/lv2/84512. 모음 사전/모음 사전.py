from itertools import product

def solution(word):
    words = []
    arr = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for comb in product(arr, repeat=i):
            words.append(''.join(list(comb)))
    words.sort()
    return words.index(word) + 1