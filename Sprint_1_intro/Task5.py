def toPostFixExpression(e):
    operators = ('-', '+', '*', '/', '%', '(', ')', '^')
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    res = []
    storage = []
    for ch in e:
        if ch not in operators:
            res.append(ch)

        elif ch == '(':
            storage.append('(')

        elif ch == ')':
            while storage and storage[-1] != '(':
                res.append(storage.pop())
            storage.pop()

        else:
            while storage and storage[-1] != '(' and priority[ch] <= priority[storage[-1]]:
                res.append(storage.pop())

            storage.append(ch)

    res.extend(storage[::-1])

    return res
