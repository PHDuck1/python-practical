def kthTerm(n, k):
    ls = set()
    i = 0

    while len(ls) < k:
        p = n ** i
        temp = {p + i for i in ls}
        ls.add(p)
        ls.update(temp)
        i += 1

    return sorted(list(ls))[k - 1]