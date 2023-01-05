def findPermutation(p, q):
    r = []
    for i in q:
        r.append(p.index(i)+1)
    return r
