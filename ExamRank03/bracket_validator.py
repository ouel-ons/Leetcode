

def isValid(s: str) -> bool:
    open = ['(', '{', '[']
    close = [')', '}', ']']
    d = {')' : '(', '}' : '{', ']': '['}
    stack = []
    for c in s:
        if c in open:
            stack.append(c)
        elif c in close:
            if not stack:
                return False
            top = stack.pop()
            if d[c] != top:
                return False
        else:
            continue
    return len(stack) == 0

print(isValid("{[()]}"))
print(isValid("[{))}]"))
print(isValid("hello(ppp)[pappap]{kkkk}"))


