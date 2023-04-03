from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr = [i  for i in range(len(dungeons))]
    arr = list(permutations(arr, len(dungeons)))
    for d in arr:
        count = 0
        t_k = k
        for i in range(len(dungeons)):
            m, u = dungeons[d[i]]  # 최소 필요, 소모 피로
            if t_k >= m:
                count += 1
                t_k -= u
            else:
                break
        answer = max(answer, count)
            
    return answer