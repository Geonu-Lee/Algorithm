def solution(people, limit):
    answer = 0
    people.sort()
    s = 0
    e = len(people) - 1
    count = 0
    while s < e:
        if people[s] + people[e] <= limit:
            count += 1
            s += 1
        e -= 1
    
    return len(people) - count