def morse_number(number):
    res = []
    for n in number:
        n = int(n)
        if n <= 5:
            encr = '.' * n + '-' * (5 - n)

        else:
            encr = '-' * (n - 5) + '.' * (10 - n)

        res.append(encr)
    return ' '.join(res)
