def evaluaterpn(tokens):
    stack = []
    for ch in tokens:
        if ch not in ["+", "-", "*", "/"]:
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == "+":
                stack.append(a+b)
            elif ch == "-":
                stack.append(a-b)
            elif ch == "*":
                stack.append(a*b)
            elif ch == "/":
                stack.append(a/b)
    return stack[-1]
tokens = ["2", "1", "+", "3", "*"]
print(evaluaterpn(tokens))
