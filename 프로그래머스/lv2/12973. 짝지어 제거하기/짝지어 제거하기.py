def solution(s):

    stack = []
    for s_ in s:
        if not stack:
            stack.append(s_)
        elif stack[-1] == s_:
            stack.pop()
        elif stack[-1] !=  s_:
            stack.append(s_)
    return 0 if stack else 1