def divide(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        if l == r:
            return p[:i+1], p[i+1:]

def check(p):  # 올바른 괄호 문자열 체크
    n = 0
    for s in p:
        if s == "(":
            n += 1
        else:
            n -= 1
        if n < 0:
            return False
    return True
        
def solution(p):
    answer = ''
    if check(p):
        return p
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        tmp_v = solution(v)
        tmp_u = u[1:-1]
        new_u = ""
        for t_u in tmp_u:
            if t_u == "(":
                new_u += ")"
            else:
                new_u += "("
        return "(" + tmp_v + ")" + new_u
