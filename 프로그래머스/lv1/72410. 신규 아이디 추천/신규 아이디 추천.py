import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z-_.]', "", new_id)
    new_id = re.sub('(([.])\\2{1,})', ".", new_id)
    if new_id[0] == ".":
        if len(new_id) == 1:
            new_id = "a"
        else:
            new_id = new_id[1:]
    if new_id[-1] == ".":
        if len(new_id) == 1:
            new_id = "a"
        else:
            new_id = new_id[:-1]
    if len(new_id) ==0:
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) < 3:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id