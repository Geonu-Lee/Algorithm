def solution(sequence, k):
    answer = []
    start, end = 0, 0
    tmp_sum = sequence[0]
    length = len(sequence)
    m = 1e09
    while start <= end < length:
        if tmp_sum == k: 
            if end - start + 1 < m:
                answer = [start, end]
                m = end - start + 1
            tmp_sum -= sequence[start]
            start += 1
        elif k > tmp_sum:
            end += 1
            if end < length:
                tmp_sum += sequence[end]
        else:
            tmp_sum -= sequence[start]
            start += 1
            
    return answer