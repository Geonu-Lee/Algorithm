def solution(players, callings):
    answer = []
    ordered = {}
    for i, p in enumerate(players):
        ordered[p] = i
    for c in callings:
        call_index = ordered[c]
        pre_player = players[call_index - 1]
        ordered[c] = call_index - 1
        ordered[pre_player] += 1
        tmp = players[call_index - 1]
        players[call_index - 1] = c
        players[call_index] = tmp
    
    return players