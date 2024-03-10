def solution(genres, plays):
    answer = []
    genres_count_dict = {}
    for i in range(len(plays)):
        if genres_count_dict.get(genres[i], 0) == 0:
            genres_count_dict[genres[i]] = plays[i]
        else:
            genres_count_dict[genres[i]] += plays[i]
    genres_count_dict = sorted(genres_count_dict.items(), key = lambda x:x[1], reverse=True)
    
    genres_dict = {}  # key: generes name, value: [index, plays]
    for i in range(len(plays)):
        if genres_dict.get(genres[i], 0) == 0:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])
        
    for k, v in genres_dict.items():
        v = sorted(v, key = lambda x:x[1], reverse=True)
        genres_dict[k] = v
    
    for name, _ in genres_count_dict:
        count = 0
        songs = genres_dict[name]
        while songs:
            if count == 2:
                break
            index, _ = songs.pop(0)
            answer.append(index)
            count += 1
            
    return answer