from collections import deque

def solution(begin, target, words):
    if not target in words:
        return 0
    q = deque()  # [words, depth]
    q.append([begin, 0])
    v = [0 for _ in range(len(words))]
    while q:
        w, d = q.popleft()
        if w == target:
            return d
        for i in range(len(words)):
            word = words[i]
            differ = 0
            if not v[i]:
                for j in range(len(word)):
                    if w[j] != word[j]:
                        differ += 1
                if differ == 1:
                    q.append([word, d + 1])
                    v[i] = 1