def divisor(n):
    i = 1
    while True:
        if n % i == 0:
            yield i
        elif i > n:
            yield None
        i += 1
