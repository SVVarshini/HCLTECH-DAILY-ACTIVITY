def isbalanced(str):
    stack = []
    for ch in str:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if( ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
                return False
    return len(stack) == 0
str = "({[]})"
print(isbalanced(str))
        
