def solution(triangle):
    d = []
    for numbers in triangle:
        d.append([0] * len(numbers))
    
    x, y = 0, 0
    d[x][y] = triangle[x][y]
    directions = [(1, 0), (1, 1)]
    for x in range(len(triangle) - 1):
        for y in range(len(triangle[x])):
            for (dx, dy) in directions:
                nx, ny = x + dx, y + dy
                number = triangle[nx][ny]
                tmp_number = d[x][y] + triangle[nx][ny]
                if d[nx][ny] < tmp_number:
                    d[nx][ny] = tmp_number
    return max(sum(d, []))