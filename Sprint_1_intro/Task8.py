def studying_hours(a):
    res = 0
    l = 0
    last = 0
    for i in a:
        if i >= last:
            l += 1
        else:
            res = max(l, res)
            l = 1

        last = i
    res = max(l, res)
    return res
